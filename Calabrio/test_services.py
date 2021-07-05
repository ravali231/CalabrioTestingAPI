import requests
import pytest
import json
from datetime import datetime

from Calabrio import identity
from Calabrio.servicequeue import Calabrioqueues
from Calabrio.ServiceQueuesCT import CreateTickets

class Test_services:

    def test_createtickets(self):
        utc_now = str(datetime.utcnow())
        print("utc time is ", utc_now)
        print("utc format time ", datetime.utcnow().strftime('%H:%M:%S'))


        # creating 4 test tickets
        self.Ticket_1 = CreateTickets.test_createticket("This is Test ticket 1")
        print("Ticket number 1 ", self.Ticket_1)
        self.Ticket_2 = CreateTickets.test_createticket("This is Test ticket 2")
        print("Ticket number 2 ", self.Ticket_2)
        self.Ticket_3 = CreateTickets.test_createticket("This is Test ticket 3")
        print("Ticket number 3 ", self.Ticket_3)
        self.Ticket_4 = CreateTickets.test_createticket("This is Test ticket 4")
        print("Ticket number 4 ", self.Ticket_4)

        # assigning racker for ticket1
        print("Ticket number 1")
        Calabrioqueues.test_assignracker(self.Ticket_1)
        # change status to In Progress for Ticket1
        Calabrioqueues.test_tktInProgress(self.Ticket_1)
        # assigning racker for ticket2
        print("Ticket number 2")
        Calabrioqueues.test_assignracker(self.Ticket_2)
        # change status to In Progress for Ticket2
        Calabrioqueues.test_tktInProgress(self.Ticket_2)
        # change status to Solved for Ticket1
        print("Ticket number 1")
        Calabrioqueues.test_tktSolved(self.Ticket_1)
        # change status to Solved for Ticket2
        print("Ticket number 2")
        Calabrioqueues.test_tktSolved(self.Ticket_2)


    def test_status(self):
        # assigning racker for ticket3
        print("Ticket number 3")
        Ticket_3 = input("Enter Ticket 3: ")
        print(Ticket_3)
        Calabrioqueues.test_assignracker(Ticket_3)
        # change status to In Progress for Ticket3
        Calabrioqueues.test_tktInProgress(Ticket_3)
        # assigning racker for ticket4
        print("Ticket number 4")
        Ticket_4 = input("Enter Ticket 4: ")
        print(Ticket_4)
        Calabrioqueues.test_assignracker(Ticket_4)
        # change status to In Progress for Ticket4
        Calabrioqueues.test_tktInProgress(Ticket_4)
        # change status to Solved for Ticket3
        print("Ticket number 3")
        Calabrioqueues.test_tktSolved(Ticket_3)
        # change status to Solved for Ticket4
        print("Ticket number 4")
        Calabrioqueues.test_tktSolved(Ticket_4)




