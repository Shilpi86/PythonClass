#data will not be stored in a single value , it will be stored in pair of values.
#pair of values=(Key,Value)
#Mutable, ordered collection and In "DICT" uses {} braces with pair of values
#                          whereas In, "SET" uses only {} with single value
d1 = {101:'abc',102:'bcd',103:'cde'}
print(type(d1))
print(d1[101])
print(d1)
d1[104]='efg' #adds the new value
d1[102]='xyz' #replacing 102 value with 'xyz'
print(d1)
d1.pop(103) # remove any values
print(d1)