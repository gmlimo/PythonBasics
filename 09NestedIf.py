#This read a number string and convert it into a number
num = int(input('Please give a number: '))

if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print("Positive Number")
else: print("Negative Number")        
