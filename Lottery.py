import random

class TicketLottery:
    
    def __init__(self):
        self.entries = {}
        
    def add_entry(self, name, tickets_requested):
        if self.entries.get(name) is None:
            self.entries[name] = tickets_requested
        else:
            print("Invalid Entry: This name has already been entered.")

    def ticket_request(self):
        name = input("What is your name?:")
        tickets = int(input("How many tickets would you like?:"))
        self.add_entry(name, tickets)
        print(name, "has been added to the entry list")
        self.ticket_menu()

    def ticket_menu(self):
        print("\nMenu")
        print("\nTo add an entry to the lottery, type 'entry'")
        print("To run the lottery, type 'run'")
        print("To find or remove a name, type 'other'")
        print("To exit, type 'exit'")
        value = input("\nPick an option:")
        if value == "entry":
            self.ticket_request()
        elif value == "run":
            tickets_available = int(input("How many tickets are available?:"))
            print("Winners:", self.run_lottery(tickets_available))
            self.ticket_menu()
        elif value == "other":
            self.name_menu()
        elif value == "exit":
            exit()
        else:
            print("Not a valid option, please try again")
            self.ticket_menu()

    def find_name(self, name):
        if self.entries.get(name) is not None:
            print(name, "is in the entry list")
        else:
            print(name, "is not in the entry list")
        self.ticket_menu()

    def remove_name(self, name):
        if self.entries.get(name) is not None:
            self.entries.pop(name)
            print(name, "has been removed from the entry list")
        else:
            print(name, "is not in the entry list")
        self.ticket_menu()

    def name_menu(self):
        name = input("What name are you looking for?:")
        value = input("Press 'f' to find the  name or 'r' to remove the name:")
        if value == "f":
            self.find_name(name)
        elif value == "r":
            self.remove_name(name)
        else:
            print("Invalid input")
        self.ticket_menu()

    def reset_lottery(self):
        self.entries = {}
                
    def run_lottery(self, tickets):
        winners = {}
        names = list(self.entries.keys())
        random.shuffle(names)
        for name in names:
            if tickets > 0:
                num = self.entries[name]
                if num <= tickets:
                    winners[name] = self.entries[name]
                    tickets = tickets - num
            else:
                break # We've used up all the available tickets
        self.reset_lottery()
        return winners

TicketLottery().ticket_menu()
