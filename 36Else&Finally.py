#Exception handling (error handling) with else and finally
import sys
try:
    a = 1
    b = 0
    if b == 0:
        raise Exception('An exception has been issued')
    c = a / b
    print('Debug: This will not be executed!!')
except Exception as err:
    print(format(err))
else:
    print('No exception found...')
finally:
    print('This block is always executed!!')
    sys.exit(0)
