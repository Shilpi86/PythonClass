# multiple classes can have multiple functions
# inheriting those multiplt classes and functions is called multiple inheritance.(

class Father:
    def home(self):
        print("Home- 2 flats and 2 plots")

class Mother:
    def cash(self):
        print("Cash-1billion")

    def jewellery(self):
        print("10kgs gold")

class Daughter(Father, Mother):
    pass

obj = Daughter()
obj.home()
obj.cash()
obj.jewellery()


