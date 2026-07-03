#The same way as Matlab does (combination of print and scanf on C)
firstName = input("What is your name? ")

print(firstName)

print('Hello {}!'.format(firstName))

age = int(input('How old are you? '))

print('Nice to meet you: {}! Your age is: {} years old'.format(firstName, age))
