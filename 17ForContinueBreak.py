#It skips 3
print('First for loop')
for i in range(5):
    if i == 3:
        continue
    print(i)

#It breaks in 3}
print('Second for loop')
for i in range(5):
    if i == 3:
        break
    print(i)
