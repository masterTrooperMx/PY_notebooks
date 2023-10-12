from vend_machine_data import beverage, stock, coins
# import only system from os
import os
# import call method from subprocess module
from subprocess import call

# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')

def fill_machine():
    stock["milk"] = 200 # ml
    stock["water"] = 300 # ml
    stock["coffee"] = 100 # g
    stock["money"] = 0 # $

def do_report():
    print('my stock', stock)

def do_quit():
    print("Good buy then!!")

def ask_money():
    pennies = int(input("how many pennies? ").lower())
    nickels = int(input("how many nicles? ").lower())
    dimes = int(input("how many dimes? ").lower())
    quarters = int(input("how many quarters? ").lower())
    return (pennies*coins["penny"] + nickels*coins["nickel"] + dimes*coins["dime"] + quarters*coins["quarter"]);

def get_attr_Bevb(attr, val):
    return next((drink for drink in beverage if drink[attr] == val), None) # builtin iterator function

def sell_beverage():
    fill_machine()
    do_report()
    game_should_continue = True
    while game_should_continue:
        guess = input("what beverage: latte, capuccino, expresso? ").lower()
        if guess == "report":
            do_report()
        elif guess == "quit":
            do_quit()
            game_should_continue = False
        elif guess == "expresso" or guess == "latte" or guess == "capuccino":
            payment = ask_money()
            beverage = get_attr_Bevb("name", guess) # lookfor entry with expresso
            price = beverage["price"]
            print("Received: ", payment, "Price:", price) # get its price
            if payment >= price and beverage != None:
                # check whether we have in stock materials to make beverage
                if stock["water"] >= beverage["water"] and stock["coffee"] >= beverage["coffee"] and stock["milk"] >= beverage["milk"]:
                    # discount all stock and add money to  stock
                    print("Thanks for you buying ", payment-price, "change")
                    stock["water"] -= beverage["water"]
                    stock["coffee"] -= beverage["coffee"]
                    stock["milk"] -= beverage["milk"]
                    stock["money"] += price
                else:
                    print("Not enought material to do beverage")
                    if stock["water"] < beverage["water"]:
                        print("not enought water ", stock["water"], beverage["water"])
                    if stock["coffee"] < beverage["coffee"]: 
                        print("not enought coffee ", stock["coffee"], beverage["coffee"])
                    if stock["milk"] < beverage["milk"]:
                        print("not enought milk ",stock["milk"], beverage["milk"])
                    print("Refounding money ", payment)
            else:
                print("Not enought money, refounding money ", payment)

sell_beverage()