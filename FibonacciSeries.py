a = 0
b = 1

i = 0

n = int(input('How many elements for the Fibonacci Series you want?: '))

while i < n:
    print(a)
    c = a + b
    a = b
    b = c
    i+=1
