#1. Given two integers M and N , write a program to print the integers from M and N.

M = 10
N = 20
for num in range(M,N):
    print(num)

#2. Write a program that reads a number N and prints the average of N numbers from 1. #Ex: N=3 then avg: 3+2+1/3

N = int(input("Enter the value of N: "))
a = []
for i in range(1,N+1):
    a.append(i)
average = sum(a) / len(a)
print("Average of list: ", round(average, 3))

#3. Given two integers M and N , write a program to print a solid rectangle pattern of M rows and N columns
# using the hash character (#)

#hollow square
print("This is the hollow square")
num = int(input("Enter the number of rows: "))
for row in range(1,num+1):
    for col in range(1,num+1):
        if row==1 or row==num or col==1 or col==num:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()

#Solid square
print("This is the solid square")
n = int(input("Enter the value: "))
for i in range(1, n + 1):
    print(" # " * n)

#solid rectangle
print("This is the solid rectangle")
m = int(input("Enter the value: "))
n = int(input("Enter the value: "))
print(" # " * m)
for i in range(1,n+1):
    print(" # " * m)

#Hollow Rectangle:

print("This is the Hollow rectangle")
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i == 1 or i == n or
                j == 1 or j == m):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()


#4. Write Program that reads a number M and N and prints N numbers after M.

m = int(input("the values of m: "))
n = int(input("the values of n: "))
print(m,n)
for i in range(m, M+n):
    print(i)

#5. Given an integer N , write a program which reads N inputs and prints the sum of the given input number.





#6. Write a program that reads a number N and prints two Right Angled Triangles of N Rows , using numbers starting from 1.

N = int(input("Enter the value of N: "))

# Right-angled Triangle 1
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Right-angled Triangle 2
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 7. Write a program that reads a number N and prints the sum of squares of N numbers starting from 1.
#Explanation: if the N=4
#The 4 numbers starting from 4 are 1,2,3,4
#Squares of those numbers are 1,4,9,16 Sum of squares are 1+4+9+16=30 Output should be 30.

n = int(input("Enter a number: "))
sum_of_squares = 0

for i in range(1, n + 1):
    print(i)
    squared_value = i ** 2
    print(str(i) + "^2 = " + str(squared_value))
    sum_of_squares += squared_value

print("Sum of squares:", sum_of_squares)
