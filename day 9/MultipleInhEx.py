# multiple classes can have multiple functions
# inheriting those multiple classes and functions is called multiple inheritance.(
# from multiple classes to one class
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


