# inheriting at many levels from different classes. ex: class A, class B(A), class C(B)
# from 1 class to new class , again from previous class to new class
class Airpod:
    def noise(self):
        print("Airpod - noise cancellation feature available")

class Airpod1(Airpod):
    def siri(self):
        print("Airpod1 - Siri feature has been added extra")

class Airpod2(Airpod1):
    def calls(self):
        print("Airpod2 - Calling feature is added extra")

    def gps(self):
        print("Airpod2 - gps is also added ")

class Airpod3(Airpod2):
    pass

obj3 = Airpod3()

obj3.noise()
obj3.siri()
obj3.calls()
obj3.gps()

