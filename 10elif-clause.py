#This read a number string and convert it into a number
num = int(input('Please give a number: '))

if num > 0:
    print("Positive Number")  
elif num == 0:  #elif is equivalent as elseif in C language  
    print('Zero')        
else: print("Negative Number")        
