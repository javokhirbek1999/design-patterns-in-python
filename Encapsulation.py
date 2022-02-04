from tokenize import Name


class Person:
    def __init__(self, name, age, gender) -> None:
        
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, name):
        self.__name = name
    
    @staticmethod
    def hello():
        print('Hello')


p1 = Person('Javokhirbek', 23, 'Male')
print(p1.Name)

p1.Name = 'Jake'

print(p1.Name)

Person.hello()
