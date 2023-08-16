#List uses the functions like print, append(add), change, delete,slice the values.
#can be changed(immutable) and [] brackets are used. Has ordered data

a1 = [12, 45, 566,'wassup',90,'hi',45] #stores the values in 0,1,2,3... index position
print(a1[:5])
print(a1[2:5])
print(a1[0:6])
print(a1)
a1.append(47394) #append the data to list
print(a1)
a1.insert(2,'list examples') #insert the value/element at specific position
print(a1)
a1[6]='same' #replacing the value at specific position
print(a1)
a1.remove(45) #removes the specific value from the list
print(a1)
a1.pop() #by default removes the last value
print(a1)
a1.pop(5) #removes the value based on index position
print(a1)
print(a1)