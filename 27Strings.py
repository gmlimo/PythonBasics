#String operations
a = 'Hello World!'
print(a)
print(a[1]) #It prints 'e'
print(a[5:8]) #It prints some words in the specified range (' Wo')

b = '   Hello there!!    '
print(b.strip()) #It will print the string without outside spaces
print(b.upper()) #It will print the string with all the letters in upper case
print(b.lower()) #It will print the string with all the letters in lower case

c = "Hi! It is me Mario"
print(c.split("!")) #Splits string in two by the marker '!' (in this case)
