class Dog:


    def __init__(self,name):
        self.name = name
        self.__a = 1
        print(self.a)

    def getName(self):
        return self.__a
    
obj1 = Dog("tommy")
print(obj1._Dog__a)

