import requests
import json
from datetime import datetime

from Calabrio import identity
from Calabrio.ServiceQueuesCT import CreateTickets


Ticketing_url = "https://stg-api.ticketing.encore.rackspace.com/v1/accounts/323676/tickets"

class Calabrioqueues:
    def test_assignracker(Ticket):

        access_token = identity.fetch_Token()

        url = Ticketing_url + "/" + Ticket
        #print(url)
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
        #print(resp_json)
        assignee = resp_json['ticket']['assignee']['value']
        #print(assignee)

        utc_now = str(datetime.utcnow())
        Ticket_assigne_time = datetime.utcnow().strftime('%H:%M:%S')
        print(Ticket + " is assigned to racker " + assignee + " at time = " + Ticket_assigne_time)
        if assignee == "rava5622":
            assert True == True
            print("Test case is assigned to racker")
        else:
            assert True == False
            print("Test case is not assigned to racker")

    def test_tktInProgress(Ticket):
        access_token = identity.fetch_Token()
        # print(access_token)
        # ticket_id = ServiceQueuesCT.test_createticket()

        url = Ticketing_url + "/" + Ticket
        #print(url)
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
        #print(resp_json)
        status = resp_json['ticket']['status']
        #print(status)

        utc_now = str(datetime.utcnow())
        Ticket_assigne_time1 = datetime.utcnow().strftime('%H:%M:%S')
        print(Ticket + " status changed to " + status + " at time = " + Ticket_assigne_time1)

        if status == "In Progress":
            assert True == True
            print("Ticket is changes to InProgress status")
        else:
            assert True == False
            print("Ticket is not changed to InProgress status")



    def test_tktSolved(Ticket):
        access_token = identity.fetch_Token()
        url = Ticketing_url + "/" + Ticket
        #print(url)
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
        #print(resp_json)
        status = resp_json['ticket']['status']
        #print(status)

        utc_now = str(datetime.utcnow())
        Ticket_assigne_time2 = datetime.utcnow().strftime('%H:%M:%S')
        print(Ticket+ " status changed to " + status + " at time = " + Ticket_assigne_time2)

        if status == "Solved":
            assert True == True
            print("Ticket is in solved status")
        else:
            assert True == False
            print("Ticket is not in solved status")











