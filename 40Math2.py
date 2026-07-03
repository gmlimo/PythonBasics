import math

'''
print('The Ceiling and Floor value of 24.55 are: '
      + str(math.ceil(24.55))
      + ' ' + str(math.floor(24.55)))
'''
'''
x = 9
y = -25
print('The value of x after copying the sign from y is: '
      + str(math.copysign(x, y)))

print('Absolute value of -86 and 52 are: '
      + str(math.fabs(-86))
      + ' ' + str(math.fabs(52)))

'''

myList = [12, 4.25, 89, 3.02,
          -65.23, -7.2, 6.3]
print('Sum of the elements of the list: ' + str(math.fsum(myList)))

print('The Greates Common Divisor of 10 and 25: '
      + str(math.gcd(10, 25)))

x = float('nan')
if math.isnan(x):
    print('It is not a number')

x = float('inf')
y = 45
if math.isinf(x):
    print('We have an infinite value')
print(math.isfinite(x)) 
print(math.isfinite(y))

print('The value of 2^8: '
      + str(math.pow(2, 8)))
print('Square root of 40000: '
      +str(math.sqrt(40000)))
print('The value of e^Pi: '
      + str(math.exp(3.14)))
print('The value of log(625), base 5: '
      +str(math.log(625, 5)))
print('The value of log(1024), base 2: '
      +str(math.log2(1024)))
print('The value of log(1024), base 10: '
      +str(math.log10(1024)))
print('The value of sin(60 degrees): '
      + str(math.sin(math.radians(60))))
print('The value of cos(pi): '
      + str(math.cos(math.pi)))
print('The angle of sin(0.8660254037844386): '
      + str(math.degrees(math.asin(0.8660254037844386))))
