import requests
import json

from Calabrio import identity
from Calabrio import ServiceQueuesCT

def test_assignracker():
    access_token = identity.fetch_Token()
    print(access_token)
    ticket_id = ServiceQueuesCT.test_createticket()

    url = "https://stg-api.ticketing.encore.rackspace.com/v1/accounts/708236/tickets/"+ticket_id
    print(url)
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    data = {

        "assignee":
            {
            "type": "racker",
            "value": "rava5622"
            }
    }
    resp = requests.put(url, headers=headers, json=data)
    resp_json = resp.json()
    print(resp_json)
    assignee = resp_json['ticket']['assignee']['value']
    print(assignee)
    if assignee == "assignee":
        assert True == True
        print("Test case is assigned to racker")
    else:
        assert True == False
        print("Test case is not assigned to racker")
    
    created_date = resp_json['ticket']['created']
    print(created_date)
    return created_date

test_assignracker()

def test_tktInProgress():
    access_token = identity.fetch_Token()
    print(access_token)
    ticket_id = ServiceQueuesCT.test_createticket()

    url = "https://stg-api.ticketing.encore.rackspace.com/v1/accounts/708236/tickets/"+ticket_id
    print(url)
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    data = {
        "status": "In Progress"

    }
    resp = requests.put(url, headers=headers, json=data)
    resp_json = resp.json()
    print(resp_json)
    status = resp_json['ticket']['status']
    print(status)
    if status == "In Progress":
        assert True == True
        print("Ticket is changes to InProgress status")
    else:
        assert True == False
        print("Ticket is not changed to InProgress status")

    created_date = resp_json['ticket']['created']
    print(created_date)
test_tktInProgress()

def test_tktSolved():
    access_token = identity.fetch_Token()
    print(access_token)
    ticket_id = ServiceQueuesCT.test_createticket()

    url = "https://stg-api.ticketing.encore.rackspace.com/v1/accounts/708236/tickets/"+ticket_id
    print(url)
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    data = {
        "status": "Solved"

    }
    resp = requests.put(url, headers=headers, json=data)
    resp_json = resp.json()
    print(resp_json)
    status = resp_json['ticket']['status']
    print(status)
    if status == "solved":
        assert True == True
        print("Ticket is in solved status")
    else:
        assert True == False
        print("Ticket is not in solved status")

    created_date = resp_json['ticket']['created']
    print(created_date)

test_tktSolved()


