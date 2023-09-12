
# introduction to Classes
class Sample: #creating a class
    a = 20
    b = 80
# allocating variables anf functions( properties) to a class.
    # you can have 'n' number classes in a file and 'n' number of properties in a class.
    def m1(self):
        print("m1")


#creating an object for class
# identifying my entire class properties info under the name 'obj'
# for one class multiple objects can be created
# for one object assign only one class
obj = Sample()
obj2 = Sample() # when you want to access and execute only 1 obj and you don't need more than one.
print(obj.a)
print(obj2.b)
print(obj.a + obj2.b)  #a+b or print(obj.a + obj.b)
obj.m1()
