from prettytable import PrettyTable # class

class MachineCoffee :
    def __init__(self) -> None:
        # it has stock material
        self.stock = {
            "water": 300,
            "coffee": 100,
            "milk": 200,
            "money": 0
        }
        # recipes to prepare beverages
        self.recipes = [
            {
                "name": "expresso",
                "water": 50,
                "coffee": 18,
                "milk": 0,
                "price": 1.5
            },
            {
                "name": "latte",
                "water": 200,
                "coffee": 24,
                "milk": 150,
                "price": 2.5
            },
            {
                "name": "capuccino",
                "water": 250,
                "coffee": 24,
                "milk": 100,
                "price": 3.0
            }
        ]
        # history
        self.history = []
    # it prepares drinks
    def prepare_drink(self):
        pass
    # it searches for recipes to prepare drinks
    def report(self):
        ingredients = []
        quantity = []
        for key in self.stock:
            ingredients.append(key)
            quantity.append(self.stock[key])
        stock_table = PrettyTable()
        stock_table.add_column("Beverage", ingredients)
        stock_table.add_column("Quantities", quantity)
        print(stock_table)