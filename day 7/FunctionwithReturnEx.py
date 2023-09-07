# return = gives the data, print = displays the data

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
def add(a,b): #passing variables as parameters
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

res = add(a,b)
res1 = sub(b,a)
print(res)
print(res1)
print(res+100) # when the function is returning the value we can use it for multiple purposes.

