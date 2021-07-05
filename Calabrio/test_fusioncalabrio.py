import requests
import json

from Calabrio import identity
from Calabrio import ServiceQueuesCT

fusion_url = "https://qa-data.fusioncloud.rackspace.net/v1/calabrio/aggticketdata/"
UTC_time = "2021-06-19T12:08:09.869000Z"

class Test_fusioncalabrio:
    def test_fusioncalabrio(self):
        access_token = identity.fetch_Token()

        self.url = fusion_url + UTC_time
        headers = {
            'Content-Type': "application/json",
            'X-Auth-Token': access_token,
            'Accept': "application/json"
        }

        resp = requests.get(self.url, headers=headers)
        resp_json = resp.json()
        print(resp_json)



