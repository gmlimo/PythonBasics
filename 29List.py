#List and its operations (List is a mutable cluster of data)
list1 = ['Apple', 'Mango', 'Banana']
print(list1)
print(list1[1]) #It prints 'Mango'

list1[2] = 'Grapes' #It changes the element 2 (Banana for Grapes)
#print(list1)

for x in list1: #Prints all elements one by one
    print(x)

if 'Apple' in list1:  #If there is 'Apple' in the list1 prints success
    print('success')

print( len(list1) )

list1.append('Blueberry') #It adds 'Blueberry' and the end of the list
print( len(list1) )
print(list1)

list1.remove('Blueberry') #It removes 'Blueberry' from the list
print( len(list1) )
print(list1)

del list1[1] #It deletes an element of a particular index
print(list1)

list1.clear() #It clear all the elements from the list
print(list1)
