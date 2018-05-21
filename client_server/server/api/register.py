"""
Flask blueprint to automatically create and share groups, then add content to those groups.
These groups can then be used to share data with an end-user.
This would be helpful during a "registration" stage when you're wiring up your users.
"""

import requests
import json
from flask import Blueprint, jsonify, request
from partnerutils.clone_utils import search_group_title
from arcgis.gis import GIS, Item

# URL to accept group invitation
ACCEPT_URL = '{0}community/users/{1}/invitations/{2}/accept'

def create_register_bp(gis):
    """Define the blueprint

    args:
    gis - a GIS object associated with YOUR admin account
    """

    bp = Blueprint("register", __name__)

    @bp.route("/group", methods=['POST'])
    def create_group():
        """Create and share a default group with the end-user"""
        jform = request.get_json()
        token = jform['token']
        schema = jform['schema']

        # construct GIS object from client-side token
        u_gis = GIS(token=token)
        

        # this is cool, urlKey is unique AND trusted because it's derived from ArcGIS token
        # I THINK you could use this to check organizational access in your own system
        # but don't quote me (definitely not a security expert)
        schema["title"] = schema["title"] + " " + u_gis.properties['urlKey']

        # get group, create if it doesn't exist
        group = search_group_title(gis, schema["title"])
        if group is None:
            group = gis.groups.create_from_dict(schema)

        # invite end-user to group
        un = u_gis.users.me.username
        group.invite_users([un])

        # accept invite on behalf of user
        url = ACCEPT_URL.format(u_gis._portal.resturl, un, group.id)
        props = {
            'token': token,
            'f': 'json'
        }
        r = requests.post(url, data=props)
        r_dict = json.loads(r.text)

        # respond
        return jsonify(r_dict)

    @bp.route("/group/<groupid>", methods=['PUT'])
    def modify_group(groupid):
        """Update a group by publishing or cloning items to that group"""
        jform = request.get_json()
        token = jform['token']
        action = jform['action']
        item_ids = jform['itemIds']
        item_map = jform.pop('itemMap', None)

        # construct GIS object from client-side token
        u_gis = GIS(token=token)
        
        items = [Item(gis, i) for i in item_ids]
        item_res = {}
        if action == 'publish':
            for i in items:
                i_clone = 
                i_pub = i.publish()
                title = i_pub.title + " " + u_gis.properties['urlKey']
                i_pub.update(item_properties={'title': title})
                i_pub.share(groups=groupid)
                item_res[i.id] = i_pub.id
            return jsonify({'itemMap': item_res})
            
            






    return bp