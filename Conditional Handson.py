# 1. Write a program that reads the students marks as input and prints PASS or FAIL.
# If the student score more than 50, print PASS.

a = int(input('Enter the marks for Maths: '))
b = int(input('Enter the marks for English: '))
c = int(input('Enter the marks for Science: '))
d = int(input('Enter the marks for Social: '))
Average = (a+b+c+d)/4
if( Average>=50):
    print('Pass')
else:
    print('Fail')

# 2. Given the length of the box, check if it is a Rectangle or Square

l = input('Enter the length of the object: ')
w = input('Enter the width of the object: ')
if(l==w):
    print("it's Square")
else:
    print('its Rectangle')

# 3 .Write a Program that reads a temperature and checks if the given temperature is
# between 15 and 40. print 'Can go for a Walk' if it is between 15 and 40.

t = int(input('Enter the weather: '))
if t in range(15,40):
    print("Can go for a walk")
else:
    print("Temperature not appropriate for walking")

# 4. Write a Program that reads the scores A and B of two players and checks if one of the
# scores is greater than 300 and the sum of the scores is less than 500.
# Print 'Can Team Up' if one the scores is greater than 300 and
# the sum of the scores is less than 500, otherwise print 'Cannot Team Up'

A = int(input('Enter player 1 scores: '))
B = int(input('Enter player 2 scores: '))
C = A+B
print(C)
if (A>300 or B >=300) and C<500:
    print('Can Team Up')
else:
     print("cannot team up")

# 5. Give three angles of a triangle, write a program to check whether the triangle is valid or not.
A1 = int(input('enter first angle : '))
A2 = int(input('enter Second angle: '))
A3 = int(input('enter Third angle: '))
S1 = input('enter the value of first side: ')
S2 = input('enter the value of Second side: ')
S3 = input('enter the value of Third side: ')
if A1+A2+A3 == 180:
    if S1 == S2 == S3:
        print("Its a Triangle")
    else:
        print("Triangle should have equal sides")
else:
    print("Its not a Triangle")

# 6.  A company decided to give a bonus of 5% to an employee if his/her years of service is
# more than five years. Write a program that reads an employee's salary and
# years of service and decides whether the employee gets the bonus or not.

sal = float(input("Enter the employee's salary: "))
exp = int(input("Enter the employee's tenure at the company: "))
if(exp>5):
    print("gets the bonus")
    print("bonus you will get is: ", (5 * sal) / 100)
else:
    print("does not qualify for bonus")

# 7.Write a program that reads a two-digit number N and checks if any of the given conditions is satisfied
# a. The sum of digits of N is equal to 7
# b. One of the digits of N is equal to 7
# c. N is divisible by 7
# d. Print "Special Number if any of the given conditions is satisfied. Otherwise, print 'Normal Number'

N = int(input("Enter the 2 digit number: "))
N1 = int(input("Enter the first digit of N: "))
N2 = int(input("Enter the second digit of N: "))
if(N1+N2)==7:
    print("special number: ")
elif(N1 or N2)==7:
    print("special number: ")
elif(N/7):
    print("special number: ")
else:
    print(N)

#or

digit = int(input("Enter the 2 digit number: "))
a=str(digit)
b=int(a[0])+int(a[1])
if b==7 or a[0]==7 or a[1]==7 or (digit%7)==0:
    print("spcl  num: ")
else:
    print("not a spcl num: ")


# 8. Write a Program that read a string S and checks if all the given conditions are satisfied
# a. The first three characters of S is NXT
# b. The remaining Characters of S contain a Number. Number is divisible by 2 or 7
# c. Print 'Special String' f any of the given conditions is satisfied. Otherwise,
# print 'Not a Special String'

S = input("Enter a string")
b = []
if S[3:]=='NXT' or S[:] or (S%2)==0 or (S%7)==0:
    print("spcl  String: ")
else:
    print("not a spcl String: ")

#9. Write a Program that read a number N and
# checks if the last digit of N is equal to the last digit of the square of N

N=int(input("Enter a number: "))
b=N**2
c=str(N)
d=str(b)
e=len(c)-1
f=len(d)-1
if c[e]==d[f]:
    print("equal")
else:
    print("not equal")


#10. Write a program that reads two numbers A and B,
#and checks if sum of squares of A and B is greater than or equals to 60.

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = a**2
d = b**2
e = c + d
if e >= 60:
    print("given number is greater than 60")
else:
    print("given number is  lesser than 60")