class Sample:
    def c1(self):
        a=10
        b=0
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
        except NameError as e1:
            print(e1)
        except Exception as e2:
            print(e2)
        try:
            print(c)
        except NameError as f:
            print(f)
obj1 = Sample()
obj1.c1()
#Handling the run time errors =  Exception handling
print("End of the Program")