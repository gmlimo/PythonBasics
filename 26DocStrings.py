#DocStrings
'''This is a single line DocString'''

def test():
    '''This is a
       multiline DocString'''
    print('test')

print(test.__doc__)
help(test)
