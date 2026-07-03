#Set is like a dictonary (is inmutable)
set1 = {'Apple', 'Microsoft', 'Amazon'}
print(set1)
#print(set1[0]) you cannot access an item of the set like this

if 'Apple' in set1:
    print('Success!')

set1.add('Yahoo') #It adds one element (only once)
print(set1)

set1.update(['Google', 'Adobe']) #It´s adds two elements
print(set1)

print(len(set1))

set1.remove('Yahoo') #It removes one element
print(set1)

set1.clear() #It deletes of the elements of the set
print(set1)

del set1 #It deletes set1 from memory
print(set1)
