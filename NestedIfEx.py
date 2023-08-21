#here the o/p will be the concat of 2 strings/2values
#the "input" function by default takes only String format
a=input("enter the value of a: ")
b=input("enter the value of b: ")
print(a+b)

#converting the data types from STR to INT and creating 2 new variables :
a=input("enter the value of a: ")
b=input("enter the value of b: ")
x=int(a)
y=int(b)
print(x+y)


#here, we  are converting String data type to integer data type instead of
# creating new 2 variables (see below):
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
print(a+b)

#checking for Login:

usrnm = input("enter the username: ")
pwd = input("enter the password: ")
if usrnm=='Python':
    if pwd=='welcome':
        print("login successful")
    else:
        print("password entered is wrong")
else:
    print("username is wrong")
