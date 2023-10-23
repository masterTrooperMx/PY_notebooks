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
    
    def do_menu(self):    
        game_should_continue = True
        while game_should_continue:
            self.coffee_machine.report()
            guess = self.show_prompt()
            if guess != "":
                if guess == "report":
                    self.coffee_machine.report()
                elif guess == "quit":
                    self.do_quit()
                    game_should_continue = False
                    print("OK good buy!")
                if game_should_continue and (guess != "report" and guess != "quit"):
                    payment = self.coin_machine.ask_payment()
                    beverage = self.coffee_machine.get_attr_Bevb("name", guess)
                    price = beverage["price"]
                    if payment-price > 0 and (guess == "expresso" or guess == "latte" or guess == "capuccino"):
                        if self.coffee_machine.stock["water"] >= beverage["water"] and self.coffee_machine.stock["coffee"] >= beverage["coffee"] and self.coffee_machine.stock["milk"] >= beverage["milk"]:
                            print("Thanks for you buying ", payment-price, "change")
                            self.coffee_machine.prepare_drink(beverage)
                            print("in money ", payment)
                        else:
                            print("Not enought material to do beverage")
                            if self.coffee_machine.stock["water"] < beverage["water"]:
                                print("not enought water ", self.coffee_machine.stock["water"], beverage["water"])
                            if self.coffee_machine.stock["coffee"] < beverage["coffee"]: 
                                print("not enought coffee ", self.coffee_machine.stock["coffee"], beverage["coffee"])
                            if self.coffee_machine.stock["milk"] < beverage["milk"]:
                                print("not enought milk ", self.coffee_machine.stock["milk"], beverage["milk"])
                            print("Refounding money ", payment)
                    else:
                        print("Not enought money, refounding money ", payment)