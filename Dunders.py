class Vector:
    # Gets executed when the object is initialized
    def __init__(self,x, y):
        self.x = x
        self.y = y

    # Gets executed when two object instances are added 
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Gets executed when the object is printed
    def __repr__(self):
        return f"({self.x},{self.y})"

    # Gets executed when the len() function is called
    def __len__(self):
        current = 0
        for i in range(100):
            current += 2
            current -= 1
        return current
    
    # Gets executed when the object is called - You can call the objects just like functions in Python :)
    def __call__(self):
        print('You are calling the object')    

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v9 = Vector(50, 50)
v3 = v1 + v2 + v9

print(v3)

print(len(v3))