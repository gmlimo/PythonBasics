#Dictionary (JSON principle)
dict1 = {'brand': 'Intel',
         'model': '8008',
         'year': '1972'}
print(dict1)
print(dict1['brand']) #It prints the brand value
print(dict1.get('model')) #Similar to above it prints the corresponding value

dict1['brand'] = 'AMD' #This updates the values
dict1['model'] = 'Ryzen'
dict1['year'] = 2017

for x in dict1: #It will print the keys (header) one by one
    print(x)

'''for x in dict1:
    print(dict(x)) '''

for x in dict1.values(): #It will print the values
    print(x)

for x, y in dict1.items(): #It will print keys and values as a pair
    print(x, y)

print(len(dict1))

dict1['color'] = 'Red' #It will add a new key and value to the dictionary
print(dict1)

dict1.clear()
del dict1
