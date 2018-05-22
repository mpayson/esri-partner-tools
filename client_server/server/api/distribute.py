"""
Flask blueprint to automatically create and share groups, then add content to those groups.
These groups can then be used to share data with an end-user.
"""

import requests
import json
from flask import Blueprint, jsonify, request
from partnerutils.clone_utils import search_group_title, clone_items_modify, search_item_title
from arcgis.gis import GIS, Item

# URL to accept group invitation
ACCEPT_URL = '{0}community/users/{1}/invitations/{2}/accept'

# Name template:
NAME_TEMPLATE = '{0} {1}'

def create_distribute_bp(gis):
    """Define the blueprint

    args:
    gis - a GIS object associated with YOUR admin account
    """

    bp = Blueprint("distribute", __name__)

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
        if group is not None:
            return jsonify({
              "WARNING": "Using existing group",
              "groupId": group.id,
              "urlKey": u_gis.properties['urlKey']
            })

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
        return jsonify({
          "groupId": group.id,
          "urlKey": u_gis.properties['urlKey']
        })

    @bp.route("/group/<groupid>", methods=['PUT'])
    def modify_group(groupid):
        """Update a group by copying or cloning items to that group"""
        jform = request.get_json()
        token = jform['token']
        copy_ids = jform.pop('copyIds', None)
        clone_ids = jform.pop('cloneIds', None)
        item_map = jform.pop('itemMap', None)

        # construct GIS object from client-side token
        u_gis = GIS(token=token)
        item_res = {}

        # callback to update title and make unique to organization
        m_callback = lambda item, t_gis: {"title": NAME_TEMPLATE.format(item.title, u_gis.properties['urlKey'])}

        # create replica then share to group, used to grant end-users access to template items but to maintain ownership
        if copy_ids:
            copy_items = [Item(gis, i) for i in copy_ids]

            paste_items = clone_items_modify(copy_items, gis, modify_item_callback=m_callback,
                                              copy_data=False, search_existing_items=False, item_mapping=item_map)
            paste_share_res = [i.share(groups=groupid) for i in paste_items]

            copy_res = {}
            for p_i in paste_items:
                src_kw = [kw.replace('source-', '') for kw in p_i.typeKeywords if 'source-' in kw][0]
                copy_res[src_kw] = p_i.id
            
            item_res['copyIds'] = copy_res

        # clone replica to end-user org then share to group, used to grant access and ownership to template items
        if clone_ids:
            clone_items = [Item(gis, i) for i in clone_ids]
            clones = clone_items_modify(clone_items, u_gis, modify_item_callback=m_callback,
                                              copy_data=False, search_existing_items=False, item_mapping=item_map)

            clone_share_res = [i.share(groups=groupid) for i in clones]

            clone_res = {}
            for cln in clones:
                src_kw = [kw.replace('source-', '') for kw in cln.typeKeywords if 'source-' in kw][0]
                clone_res[src_kw] = cln.id
            
            item_res['cloneIds'] = clone_res

        return jsonify(item_res)


    return bp