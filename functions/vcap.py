import os, json

def getService(name):
    if 'VCAP_SERVICES' in os.environ:
        vcap = json.loads(os.getenv('VCAP_SERVICES'))
        print('Found VCAP_SERVICES')
        if name in vcap:
            creds = vcap[name][0]['credentials']
            user = creds['username']
            password = creds['password']
            url = 'https://' + creds['host']
            return (user, password, url)
    elif os.path.isfile('vcap-local.json'):
        with open('vcap-local.json') as f:
            vcap = json.load(f)
            print('Found local VCAP_SERVICES')
            creds = vcap['services'][name][0]['credentials']
            user = creds['username']
            password = creds['password']
            url = 'https://' + creds['host']
            return (user, password, url)

