#Exception handling (knowing the type of error handled)
try:
    a = 1
    b = 0
    c = a / b
    print('Debug: This will not be executed!!')
except ZeroDivisionError as err:
    print(format(err))
except TypeError as err:
    print(format(err))
except Exception:
    print('Exception Encounterd!')

print('Debug: This will be executed!!')
