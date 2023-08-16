#List Handson project
#1) The prefilled code contains a list. You need to write a program to read N integers, and
# print the elements at the index locations represented by those integers.
#Input:
#The first line of input will contain a positive integer(N)
#The following N lines will contain a positive number in each line.
# Explanation:
#If the given number is 2, read the inputs in the next two lines and
# print the elements at the given indexes. If the given two indexes are 1 and 4

a = ['Python', 'Java', 'Ruby', 'Move', 'C++', 'Go', 'C', 'R', 'Swift', 'perl']
print(a)
print(a[0])
print(a[0:10])
N=92
if N%5==0:
    print(N,"is divisible by 5")
else:
    print(N,"is not divisible by 5")

#----------------------------------------------------------------------------------------------
#2)
#Write a program to print last 3 inputs.
n = ['hi',28,'wish',90,90.4,'welcome',70]
a = 3
res = n[-a:] #prints only last 3 inputs
print(res)


# print the list containing first and last 3 inputs
n = ['hi',28,'wish',90,90.4,'welcome',70]
res = n[0],n[4:] #prints only last 3 inputs
print(res)

#or

#n = ['hi',28,'wish',90,90.4,'welcome',70]
#res = n[0]
#last_two_str = str(n)[-20:]
#result = str(last_two_str) # str to int
#print(n[0] , result)

#Write a program to read N inputs and print first input.
n = ['hi',28,'wish',90,90.4,'welcome',70]
print(n)
print(n[0])

#-----------------------------------------------------------------------------------------------------
#3) Given a number N , write a program that read N numbers and
# prints a list of numbers that are divisible by 5.

N = [2,5,35,46,768,90,65,100]
print(N)
for x in N:
    if x%5==0:
        print(x)

#------------------------------------------------------------------------------------------------------
#4)A List L is given in the prefilled code.
#Given a number N , write a program that reads N inputs and
#prints the list by adding a given N inputs at the end of the list L.

L = ["apple", 78, 970.03]
N = [2,5,35,46,768,90,65,100]
print(N)
res = L+N
print("Concatenated list:\n" + str(res))

#or

L = ["apple", 78, 970.03]
N = [2,5,35,46,768,90,65,100]
print(N)
L.append(N)
print("Concatenated list:\n" + str(L))

#or

L = ["apple", 78, 970.03]
N=2
L.append(N)
print("Concatenated list:\n" + str(L))

#-------------------------------------------------------------------------------------------------------
#5)Create a list, Given a number N, write a program that prints the list by repeating the List N times.

V = [2,5,35,46,768,90,65,100]
N=5
list_new = V*N
print(list_new)

#------------------------------------------------------------------------------------------------------
#6)Given N number, and an index, write a program to store the numbers in a list and
# print the number at the given index. For this problem, each input will contain T test cases.
# Each test case will give an index Ki as input, which should be considered to print the number
#Input:
#The first line of input is an integer N
#The second line of input is an integer T representing the number of test cases
#The Next lines contains integers representing the numbers of list.
#The next T lines contains integer Ki for each line.
#Output:
#You need to print a number in a new line for each of the K test cases.

a1 = [1,5,8,10]
