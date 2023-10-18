from prettytable import PrettyTable # class
from classes.MachineCoffee import MachineCoffee # class
from classes.MachineCoins import CoinMachine # class

class Menu:
    def __init__(self) -> None:
        self.coffee_machine = MachineCoffee()
        self.coin_machine = CoinMachine()
        # has menu to display
        # has menu item to capture
        pass

    def do_quit(self):
        print("Good buy then!!")

    def show_prompt(self):
        return input("what beverage: latte, capuccino, expresso? ").lower()
    
    def define_option(self, input):
        if(input != ""):
            if input == "report":
                self.coffee_machine.report()
            elif input == "quit":
                self.do_quit()
        
        return False
    
    def do_menu(self):    
        game_should_continue = True
        while game_should_continue:
            self.coffee_machine.report()
            guess = self.show_prompt()
            payment = self.coin_machine.ask_payment()
            print("in money ", payment)
            game_should_continue = self.define_option(guess)
        print("OK good buy!")