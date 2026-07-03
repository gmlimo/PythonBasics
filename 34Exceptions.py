#Exception handling (error handling)
try:
    a = 1
    b = 0
    c = a / b
    print('Debug: This will not be executed!!')
except Exception:
    print('Exception Encounterd!')

print('Debug: This will be executed!!')
