class Animal:
    def __init__(self) -> None:
        self.eyes = 2
        self.tail = 1
    # to print out an object
    def __str__(self) -> str:
        return str(f"class Animal: \neyes {self.eyes}, tail {self.tail}, \nmethods: breath()\n")
    
    def breath(self):
        print("inhale-exhale")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__() # 2 eyes and 1 tail
        self.fins = 2
    # to print out an object
    def __str__(self) -> str:
        return super().__str__() + str(f"class Fish: \neyes {self.eyes}, tail {self.tail}, fins {self.fins} \nmethods: swim()\n")
    # overloading breath
    def breath(self):
        super().breath()
        print("filter water instead air.")
    
    def swim(self):
        print("move in water")

# instances
donkey = Animal()

nemo = Fish()
# print object
print(donkey)
print(nemo)
# methods
donkey.breath()
nemo.breath()