import requests
import json

from Calabrio import identity

def test_createticket():
    access_token = identity.fetch_Token()
    print(access_token)

    url = "https://stg-api.ticketing.encore.rackspace.com/v1/accounts/708236/tickets"
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    data = open("data1.json", "r").read()
    json_request = json.loads(data)
    resp = requests.post(url, headers=headers, json=json_request)
    resp_json = resp.json()
    ticket_id = resp_json['ticket']['ticket_id']

    created_date = resp_json['ticket']['created']
    print(created_date)
    print(ticket_id)
    return ticket_id

#changes queues while running the tickets

test_createticket()

