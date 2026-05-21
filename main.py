#SECTİON-1: DECORATORS

print("="*60)
print("SECTİON-1: DECORATORS")
print("="*60)


def my_decorator(func):
    def wrapper():
        print("wrapper function executed")
        func()
        print("wrapper function executed")

    return wrapper

@my_decorator
def hello_world():
    print("hello world")

hello_world()


#-----------------------------------------------------------------
#SECTİON-2: PROPERTY DECORATORS

print("="*60)
print("SECTİON-2: PROPERTY DECORATORS")
print("="*60)

#data validation, private/public (encapsulation)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    #getter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        if len (value) < 3:
            raise ValueError("name should be longer")
        self.__name = value

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("age must be an integer")
        if value < 0:
            raise ValueError("age must be positive")
        if value > 150:
            raise ValueError("age must be less than 150")
        self.__age = value



atil = Person("Atil", 60)
print(atil.name)
atil.name="Atil Samancıoglu"
print(atil.name)
del atil.name
print(atil.name)
print(atil.age)
atil.age=15
print(atil.age)

try:
    atil.age = 155
except ValueError as e:
    print("Hata:", e)

try:
    atil.age = -20
except ValueError as e:
    print("Hata:", e)


#-----------------------------------------------------------------
#SECTİON-3: STATİC METHOD
#instance oluşturmadan kullanılan methodlardır. sınıf içindeki instance'lar ile ilgileri yoktur.
#Herhangi bir değişiklik yapmazlar.


print("="*60)
print("SECTİON-3: STATIC METHOD")
print("="*60)


class MathOperation:
    @staticmethod
    def add(x, y):
        return x + y

math = MathOperation() #instance oluşturma, ancak buna gerek yok. bu "self" kullanıldığında gerekir çünkü self instance'a referans verir.
print(math.add(1, 2))

print(MathOperation.add(1, 2))


#--------------------------------------------------------------------
#SECTİON-4: CLASS METHOD
#sınıfın içindeki deüişekene ulaşma

print("="*60)
print("SECTİON-4: CLASS METHOD")
print("="*60)

#alternative constructor

class Pizza:
    total_pizza = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.total_pizza +=1

    @classmethod
    def margherita(cls):
        return cls(["peynir","domates","feslegen"])

    @classmethod
    def pepperoni(cls):
        return cls(["peynir", "domates", "sucuk"])

    @classmethod
    def get_total_pizza(cls):
        return cls.total_pizza


pizza1 = Pizza.margherita()
print(pizza1.ingredients)
pizza2 = Pizza.pepperoni()
print(pizza2.ingredients)
print(Pizza.get_total_pizza())