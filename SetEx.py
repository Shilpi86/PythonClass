#Unordered collection (prints data randomly), Mutable (with restrictions-only add/Remove data),{} braces
#Index positional concepts are not accessible in Set
S={23,'hello',67,90,100}
print(type(S))
print(S)
S.add(200)
print(S)
S.remove(100)
print(S)

#cannot use append and can be used if you just need 'to access the info regardless of the order