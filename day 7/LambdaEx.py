def myfunc(n):
  return lambda a : a * n #lambda is used only when an function has to be used anonymously for short period of time.

mydoubler = myfunc(2)

print(mydoubler(11))

#ex 2:
x = lambda a, b : a * b
print(x(5, 6))

#or

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))