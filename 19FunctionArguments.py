#Function with one argument
def printHello( firstName ):
    print("Hello {}!!".format(firstName))
    
#Function with two arguments
def suma(a, b):
    sumaOp = a + b
    print("El resultado es: {}".format(sumaOp))

#Function with a default argument
def circleArea(r, pi = 3.1416):
    area = pi*r**2
    print("El área del círculo es: {}".format(area))

printHello('Wyatt')
suma(7, 3)
circleArea(2.5) #If pi is not used a default value is already passed
circleArea(5, 3) #Here the value of pi is set to 3
