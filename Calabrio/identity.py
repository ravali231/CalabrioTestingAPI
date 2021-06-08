import json
import os
import requests


def fetch_Token():
    url = 'https://staging.identity-internal.api.rackspacecloud.com/v2.0/tokens'
    data = open("data.json","r").read()
    json_request = json.loads(data)

    r = requests.post(url, json=json_request)
    return r.json()['access']['token']['id']

fetch_Token()