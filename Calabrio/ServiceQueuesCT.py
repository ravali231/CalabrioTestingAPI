import requests
import json

from Calabrio import identity
from datetime import datetime

class CreateTickets:
    def test_createticket(sub):
        access_token = identity.fetch_Token()
        # print(access_token)

        url = "https://stg-api.ticketing.encore.rackspace.com/v1/accounts/323676/tickets"
        headers = {
            'Content-Type': "application/json",
            'X-Auth-Token': access_token,
            'Accept': "application/json"
        }
        data = {
            "subject": sub, "description": "This is a description for a test ticket", "category_id": "10",
            "sub_category_id": "33"
            , "group": "Quality Engineering", "classification": "Incident", "products": [
                "https://prodrackspacesupport.service-now.com/nav_to.do?uri=%2Fcmdb_ci_list.do%3Fsysparm_query%3Du_account_id%253Db263589e-eba1-47f0-acc4-a15d857d8c05"]
        }

        # data = open("data1.json", "r").read()
        # json_request = json.loads(data)
        resp = requests.post(url, headers=headers, json=data)
        resp_json = resp.json()
        ticket_id = resp_json['ticket']['ticket_id']

        created_date = resp_json['ticket']['created']

        print("Created date ", created_date)
        print(ticket_id)
        return ticket_id



    '''
        utc_now = datetime.utcnow()

        dt = datetime.strptime(utc_now, '%Y-%m-%d %H:%M:%S.%f')
        print(dt)
        datetime.strptime(utc_now,"%H:%M:%S")
        print("utc time is " + utc_now)
    '''

    # Global Windows - Fazure
    # account - 708236
    # "category_id": "ord-0002312", "sub_category_id": "ord-0001616"
    # changes queues while running the tickets



