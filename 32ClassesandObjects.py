class Point:
    
#constructor of the class
    def __init__(self, x = 0, y = 0, z = 0):
        self.assign(x, y, z)
        
#A getter method
    def assign(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def printPoint(self):
        print(self.x, self.y, self.z)

#Creating some objects (instances)
p1 = Point()
p1.printPoint()

print(type(p1))

p1.assign(1, 1, 2)
p1.printPoint()

p2 = Point(2, 3, 4)
p2.printPoint()
