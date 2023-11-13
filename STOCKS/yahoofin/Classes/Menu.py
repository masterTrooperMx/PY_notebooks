from Classes.Portfolio import *

portfolio = Portfolio()

class Menu():
    def __init__(self) -> None:
        pass

    def do_quit(self):
        print("Nice stocks girl!!")

    def show_prompt(self):
        return input("what option: symbols, graphs, analysis? ").lower()
    
    def display_symbols(self):
        print(portfolio.get_symbols())

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
                if choice == "analysis":
                    self.do_analysis()
    