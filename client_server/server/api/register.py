"""
Flask blueprint to automatically create and share groups, then add content to those groups.
These groups can then be used to share data with an end-user.
This would be helpful during a "registration" stage when you're wiring up your users.
"""

import requests
import json
from flask import Blueprint, jsonify, request
from partnerutils.clone_utils import search_group_title
from arcgis.gis import GIS

# URL to accept group invitation
ACCEPT_URL = '{0}community/users/{1}/invitations/{2}/accept'

# GROUP template configurations
group_title = 'My Test {0}'
group_schema = {
    "title": "My Test Title",
    "tags": "test, group, poc, scripts",
    "description": "Test group for partner python scripts",
    "access": 'private',
    "is_invitation_only": True,
    "users_update_items": False
}

def create_register_bp(gis):
    """Define the blueprint

    args:
    gis - a GIS object associated with YOUR admin account
    """

    bp = Blueprint("register", __name__)

    @bp.route("/group", methods=['POST'])
    def create_group():
        """Create and share a group with the end-user"""
        jform = request.get_json()
        token = jform['token']

        # construct GIS object from client-side token
        u_gis = GIS(token=token)
        
        schema = dict(group_schema)

        # this is cool, urlKey is unique AND trusted because it's derived from ArcGIS token
        # I THINK you could use this to check organizational access in your own system
        # but don't quote me (definitely not a security expert)
        schema["title"] = group_title.format(u_gis.properties['urlKey'])

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

    # @bp.route("/group")

    return bp