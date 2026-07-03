def averageN():
    N = int(input('How many elements will you have?: '))

    i = 0
    suma = 0

    while i < N:
        print('Give data{}: '.format(i))
        d = int(input(''))
        suma = suma + d
        i+=1
    P = suma / N
    print('The average is: ', P)

averageN()
