class CoinMachine:
    def __init__(self) -> None:
        self.coins = {
            "penny": 0.01,
            "nickel": 0.05,
            "dime": 0.1,
            "quarter": 0.25
        }
    
    def ask_payment(self):
        pennies = int(input("how many pennies? ").lower())
        nickels = int(input("how many nicles? ").lower())
        dimes = int(input("how many dimes? ").lower())
        quarters = int(input("how many quarters? ").lower())
        return (pennies*self.coins["penny"] + nickels*self.coins["nickel"] + dimes*self.coins["dime"] + quarters*self.coins["quarter"]);
