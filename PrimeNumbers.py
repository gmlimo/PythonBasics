lower = 2
upper = 100

'''Identation is very important here, if misplaced, program
does not work as expected'''
for num in range(lower, upper+1):
    for i in range(2, num):
        if(num % i) == 0:
            break
    else:
        print(num)
