#Tuple: A kind of inmutable cluster of data
tuple1 = ('Batman', 'Superman', 'Wonder Woman')
print(tuple1) #Prints all the tuple
print(tuple1[0]) #It prints Batman

'''tuple1[0] = 'IronMan' this line shows error, because you cannot change elements
in a tuple (is inmutable) '''

for x in tuple1:  #To print values one by one
    print(x)

print( len(tuple1) ) #size of the tuple
del tuple1 #deletes tuple from memory
#print(tuple1)
