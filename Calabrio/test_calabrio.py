import requests
import json
from datetime import datetime

from Calabrio import identity
#from Calabrio import ServiceQueuesCT
from Calabrio import Servicequeues

def test_createtickets():
    utc_now = str(datetime.utcnow())
    print("utc time is ", utc_now)
    print("utc format time ", datetime.utcnow().strftime('%H:%M:%S'))
    #Ticket_1 = ServiceQueuesCT.test_createticket("This is Test ticket 1")
    Ticket_1 = "210618-iad-0000034"

    print("Ticket number 1 ",Ticket_1)

    # assigning racker for ticket1
    print("Ticket number 1")
    Servicequeues.test_assignracker(Ticket_1)
    # change status to In Progress for Ticket1
    Servicequeues.test_tktInProgress(Ticket_1)
    # change status to Solved for Ticket1
    Servicequeues.test_tktSolved(Ticket_1)

test_createtickets()

'''
    Ticket_2 = ServiceQueuesCT.test_createticket("This is Test ticket 2")
    print("Ticket number 2 ", Ticket_2)
    Ticket_3 = ServiceQueuesCT.test_createticket("This is Test ticket 3")
    print("Ticket number 3 ", Ticket_3)
    Ticket_4 = ServiceQueuesCT.test_createticket("This is Test ticket 4")
    print("Ticket number 4 ", Ticket_4)

    #assigning racker for ticket1
    print("Ticket number 1")
    Servicequeues.test_assignracker(Ticket_1)
    #change status to In Progress for Ticket1
    Servicequeues.test_tktInProgress(Ticket_1)
    # assigning racker for ticket2
    print("Ticket number 2")
    Servicequeues.test_assignracker(Ticket_2)
    # change status to In Progress for Ticket2
    Servicequeues.test_tktInProgress(Ticket_2)
    # change status to Solved for Ticket1
    print("Ticket number 1")
    Servicequeues.test_tktSolved(Ticket_1)
    # change status to Solved for Ticket2
    print("Ticket number 2")
    Servicequeues.test_tktSolved(Ticket_2)
'''

#test_createtickets()



'''
def test_status():
    # assigning racker for ticket3
    print("Ticket number 3")
    Servicequeues.test_assignracker(test_createtickets().Ticket_3)
    # change status to In Progress for Ticket3
    Servicequeues.test_tktInProgress(test_createtickets().Ticket_3)
    # assigning racker for ticket4
    print("Ticket number 4")
    Servicequeues.test_assignracker(test_createtickets().Ticket_4)
    # change status to In Progress for Ticket4
    Servicequeues.test_tktInProgress(test_createtickets().Ticket_4)
    # change status to Solved for Ticket3
    print("Ticket number 3")
    Servicequeues.test_tktSolved(test_createtickets().Ticket_3)
    # change status to Solved for Ticket4
    print("Ticket number 4")
    Servicequeues.test_tktSolved(test_createtickets().Ticket_4)

'''
#test_status()
