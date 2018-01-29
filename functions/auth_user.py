#
# functions to auth login
#

import json, os

def auth(username, password):

    if password == "IBM@123" and username == "aoun":
        return True, 1
    else:
        return False, None

def checkID(id):

    client = getClient()
    users_db = client['users']
    
    for u in users_db:
        if u['id']==id:
            client.disconnect()
            return ({"name":u['name'], "password":u['password'], "id":u['id']})
