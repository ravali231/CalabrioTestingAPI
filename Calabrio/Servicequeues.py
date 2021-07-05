import requests
import json
from datetime import datetime

from Calabrio import identity
from Calabrio import ServiceQueuesCT

Ticketing_url = "https://stg-api.ticketing.encore.rackspace.com/v1/accounts/323676/tickets"
'''
def test_createtickets():
    utc_now = str(datetime.utcnow())
    print("utc time is ", utc_now)
    print("utc format time ", datetime.utcnow().strftime('%H:%M:%S'))
    Ticket_1 = ServiceQueuesCT.test_createticket("This is Test ticket 1")
    print("Ticket number 1 ",Ticket_1)
    Ticket_2 = ServiceQueuesCT.test_createticket("This is Test ticket 2")
    print("Ticket number 2 ", Ticket_2)
    Ticket_3 = ServiceQueuesCT.test_createticket("This is Test ticket 3")
    print("Ticket number 3 ", Ticket_3)
    Ticket_4 = ServiceQueuesCT.test_createticket("This is Test ticket 4")
    print("Ticket number 4 ", Ticket_4)


test_createtickets()
'''

def test_assignracker(Ticket):
    access_token = identity.fetch_Token()
    #print(access_token)
    #ticket_id = ServiceQueuesCT.test_createticket()
    print("Test",Ticket)
    url = Ticketing_url+"/"+ Ticket
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

    utc_now = str(datetime.utcnow())
    Ticket_assigne_time = datetime.utcnow().strftime('%H:%M:%S')
    Ticket + "is assigned to racker" +assignee + "at time =" + Ticket_assigne_time
    if assignee == "assignee":
        assert True == True
        print("Test case is assigned to racker")
    else:
        assert True == False
        print("Test case is not assigned to racker")
    
    #created_date = resp_json['ticket']['created']
    #print(created_date)
    #return created_date

test_assignracker("tes")

def test_tktInProgress(Ticket):
    access_token = identity.fetch_Token()
    #print(access_token)
    #ticket_id = ServiceQueuesCT.test_createticket()

    url = Ticketing_url +"/"+Ticket
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

    utc_now = str(datetime.utcnow())
    Ticket_assigne_time1 = datetime.utcnow().strftime('%H:%M:%S')
    Ticket + "status changed to" + status + "at time =" + Ticket_assigne_time1

    if status == "In Progress":
        assert True == True
        print("Ticket is changes to InProgress status")
    else:
        assert True == False
        print("Ticket is not changed to InProgress status")

    #created_date = resp_json['ticket']['created']
    #print(created_date)
test_tktInProgress("")

def test_tktSolved(Ticket):
    access_token = identity.fetch_Token()
    #print(access_token)
    #ticket_id = ServiceQueuesCT.test_createticket()

    url = Ticketing_url+"/"+Ticket
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

    utc_now = str(datetime.utcnow())
    Ticket_assigne_time2 = datetime.utcnow().strftime('%H:%M:%S')
    Ticket + "status changed to" + status + "at time =" + Ticket_assigne_time2

    if status == "solved":
        assert True == True
        print("Ticket is in solved status")
    else:
        assert True == False
        print("Ticket is not in solved status")

    #created_date = resp_json['ticket']['created']
    #print(created_date)

test_tktSolved("")


