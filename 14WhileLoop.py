#Prints the numbers 0-9

print('i part')
i = 0

while i < 10:
    print(i)
    i += 1

#Here a while break is introduced. The while breaks on 5
print('k part')
k = 0

while k < 10:
    print(k)
    if k == 5:
      break
    k = k + 1
    
#The number 7 is skipped in this loop
print('m part')
m = 0

while m < 10:
    m = m + 1
    if m == 7:
        continue
    print(m)
