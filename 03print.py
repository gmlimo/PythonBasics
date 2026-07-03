#Uses of the print function
pi = 3.14
print('The value of pi is: ', pi)

#print function works similar to C language ...not working % pi
print('The angle is: %f radians', (pi))

#This gets the work done
print('Value of Pi is {} radians'.format(pi))

firstName = 'Martin'
lastName = 'Limon'

print('My name is: {} {}.'.format(firstName, lastName))

#The order of the strings can change like this:

print('My name is: {1} {0}.'.format(firstName, lastName))
