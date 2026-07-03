class myError(Exception):
    pass

class ValueTooSmallError(myError):
    pass

class ValueTooLargeError(myError):
    pass

number = 10

try:

    i_num = int(input('Give me an integer number: '))

    if i_num < number:
        raise ValueTooSmallError
    if i_num > number:
        raise ValueTooLargeError
    else:
        print('Good')

except ValueTooSmallError:
    print('Value is smaller than expected!!')

except ValueTooLargeError:
    print('Value is bigger than expected!!')

except Exception as error:
    print(format(error))
        
finally:
        print('Program finished')
