
#Write a program to print last 3 inputs.
n = ['hi',28,'wish',90,90.4,'welcome',70]
a = 3
res = n[-a:] #prints only last 3 inputs
print(res)


# print the list containing first and last 3 inputs
n = ['hi',28,'wish',90,90.4,'welcome',70]
a = 3
res = n[0],n[-a:] #prints only last 3 inputs
print(res)


#Write a program to read N inputs and print first input.
n = ['hi',28,'wish',90,90.4,'welcome',70]
print(n)
print(n[0])