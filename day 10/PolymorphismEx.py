class Iphone_SE2ndgeneration:
    def Size(self):
        print("4.7")
    def Camera(self):
        print("12MP")
    def Battery_Life(self):
        print("13h")
    def Chip(self):
        print("A13")
class Iphone_SE3rdgeneration(Iphone_SE2ndgeneration):
    def Size(self):
        print("4.7")
    def Camera(self):
        print("12MP")
    def Battery_Life(self):
        print("15h")
    def Chip(self):
        super().Chip()
    def network(self):
        print("5G")
obj1 = Iphone_SE3rdgeneration()
obj1.Size()
obj1.Camera()
obj1.network()
obj1.Chip()
obj1.Battery_Life()
