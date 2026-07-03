
class Person:
    def method1(self, a, b, c):
        self.var1 = a
        self.var2 = b
        self.var3 = c
        
obj1 = Person()
obj1.method1(1, 2, 3)
print(obj1.var1, obj1.var2, obj1.var3)

class Employee(Person): #Inheritance
    pass

obj2 = Employee()
obj2.method1(3, 1, 2)
print(obj2.var1, obj2.var2, obj2.var3)
