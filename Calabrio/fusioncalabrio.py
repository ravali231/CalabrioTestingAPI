import requests
import json

from Calabrio import identity
from Calabrio import Servicequeues

def test_fusioncalabrio():
    access_token = identity.fetch_Token()
    print(access_token)
    created_date = Servicequeues.test_assignracker()

    url = "https://qa-data.fusioncloud.rackspace.net/v1/calabrio/aggticketdata/"+created_date
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }

    resp = requests.get(url, headers=headers)
    resp_json = resp.json()
    #print(resp_json)

test_fusioncalabrio()
