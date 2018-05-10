"""utility functions to assist with adding users"""
import csv

USER_FIELDS = ["username", "password", "firstname", "lastname", "email", "role", "groups",
               "groups", "description", "role", "provider", "idp_username", "level"]

def add_user(user, gis, groups=None, field_map=None):
    """Add user to the gis
    * Abstraction for creating from dict such as with csv
    * Handles moving to groups

    args:
    user -- a dictionary containing user fields, see fields:
    http://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#arcgis.gis.UserManager.create
    gis -- gis object where users are added
    groups -- (optional) destination groups, compliments those in dict (default [])
    field_map -- (optional) change keys from defaults in USER_FIELDS to those in dict
    """

    # set defaults
    groups = groups if groups else []
    field_map = field_map if field_map else {}

    try:

        # Define new user fields
        new_user = {}
        for field in USER_FIELDS:
            new_user[field] = (user.get(field_map[field], None)
                               if field in field_map
                               else user.get(field, None))

        print("INFO: Creating user {}".format(new_user["username"]))

        # Create/augment array of destination groups for user
        # Pop group from user because separate logic
        group_field = field_map["groups"] if "groups" in field_map else "groups"
        group_str = new_user.pop(group_field, None)
        if group_str:
            group_list = group_str.split(",")
            for g in group_list:
                group_search = gis.groups.search(g)
                if group_search:
                    groups.append(group_search[0])

        # Create new user
        result = gis.users.create(**new_user)

        # Sometimes there's an error that doesn't throw
        if not result:
            return

        # Add user to groups
        for g in groups:
            try:
                g.add_users([new_user['username']])
            except Exception as e:
                print("ERR: Could not add user to group {}".format(g))
                print(e)

        return result

    except Exception as e:
        print("ERR: Could not create user {}".format(user['username']))
        print(e)

def add_users_csv(csv_file, gis, groups=None, field_map=None):
    """Add users from csv to gis
    * Convenient abstraction for csvs

    args:
    csv_file -- path to csv with users to create
    gis -- gis object where users are added
    groups -- (optional) destination groups, compliments those in csv (default [])
    field_map -- (optional) change keys from defaults in USER_FIELDS to those in csv, see fields:
    http://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#arcgis.gis.UserManager.create
    """
    results = []
    with open(csv_file, 'r') as users_csv:
        users = csv.DictReader(users_csv)
        for user in users:
            result = add_user(user, gis, groups=groups, field_map=field_map)
            results.append(result)
    
    return results