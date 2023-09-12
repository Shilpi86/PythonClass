class demo:
    def m1(self):
        print("m1 function")

class sample():
    def m2(self):
        print("m2 function")
# generally, we dont use one obj to 2 or more classes, but there is an indirect approach to do this.
obj1 = demo()
obj2 = sample()
obj1.m1()
obj2.m2()

#in order to do that , we have to use inheritance.
# sample class(child) is inherited into demo(parent) class
# use class sample(demo): (check above)
# Single inheritance , no dependency

class demo:
    def m1(self):
        print("m1 function")

class sample(demo):
    def m2(self):
        print("m2 function")
# generally, we dont use one obj to 2 or more classes, but there is an indirect approach to do this - inheritance.
obj1 = demo()
obj1 = sample()
obj1.m1()
obj1.m2()

