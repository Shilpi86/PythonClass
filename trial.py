#5. Given an integer N , write a program which reads N inputs and prints the sum of the given input number.

n = int(input("Enter a number: "))
sum_of_squares = 0

for i in range(1, n + 1):
    print(i)
    squared_value = i ** 2
    print(str(i) + "^2 = " + str(squared_value))
    sum_of_squares += squared_value

print("Sum of squares:", sum_of_squares)
n = int(input("print the number: "))
sum = 0
for i in range(1, n+1):
    sum = sum+i
    print(sum)

