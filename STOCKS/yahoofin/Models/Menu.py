import json
from Models.Portfolio import *

portfolio = Portfolio()

class Menu():
    def __init__(self) -> None:
        # import values from  config file
        with open('./conf.json') as conf_file:
            file_contents = conf_file.read()
        parsed_json = json.loads(file_contents)
        print("reading config file ...")
        symbol = []
        for stock in parsed_json:
            if 'name' in stock:
                symbol.append(stock["name"])
            else:
                portfolio.startdate = stock["startdate"]
                portfolio.enddate   = stock["enddate"]
        portfolio.set_symbols(symbol)
        print(portfolio.get_symbols())
        portfolio.check_file(portfolio.startdate, portfolio.enddate, True, True)
        print("excuting config options")

    def do_quit(self):
        print("Nice stocks girl!!")

    def show_prompt(self):
        return input("what option: symbols, data, graphs, analysis? ").lower()
    
    def display_symbols(self):
        print(portfolio.get_symbols())

    def display_data(self):
        symbol = input(f"what symbol: {portfolio.get_symbols()} ").upper()
        print(f"getting info from {symbol}")
        portfolio.portfolio_show_data(symbol)
        
    def do_analysis(self):
        # working with df in order to have info 
        pass

    def do_menu(self):
        follow_compute = True
        while follow_compute:
            choice = self.show_prompt()
            if choice != "":
                if choice == "quit":
                    self.do_quit()
                    follow_compute = False
                if choice == "symbols":
                    self.display_symbols()
                if choice == "data":
                    self.display_data()
                if choice == "analysis":
                    self.do_analysis()
    