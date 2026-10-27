class Chai:
    origin = "India"

tea = Chai()
# object

tea.origin = "US"

print(tea.origin)
print(Chai.origin)
# objects are instance of a class , they have their own namespace
# changing origin of tea object wont change the Chai origin class variable.



tea.strength = 'strong'


del tea.origin
del tea.strength
print(tea.origin)
# will get India , why because , even though tea object had origin as US , we deleted it so it fallback to its default which was India
# print(tea.strength)
# ERROR -> because Chai class itself doesnt have any class members named strength



class Student:
    name = 'Swaraj'

    # always use self inside class functions , self refers to the whole class and its member variables and methods.
    # its similar to this in java.
    def print_name(self):
        print(f"Name is {self.name}")


student1 = Student()
student2 = Student()


student1.print_name()
# will print correctly
# Student.print_name()
# will give an error, because for calling functions using class name , u need to pass the reference , WHY SO???


# FOR EXAMPLE

student2.name = 'Yuvraj'

# Student.print_name()
# ERROR
# WHICH STUDENT??? print_name doesnt have any idea which object it refers to

# when we call student1.print_name()
# by default the reference of the object which is student1 is sent , so it knows that name is Swaraj

# but if we just call Student.print_name()
# we dont know which Student to refer to


Student.print_name(student1)
Student.print_name(student2)




# for constructor we use __init__


class Teacher:
    def __init__(self , name):
        self.name = name

    def list_teachers(self):
        print(self.name)

teacher1 = Teacher("Einstein")
teacher2 = Teacher("Hawking")

teacher1.list_teachers()
teacher2.list_teachers()

# inheritance

class BaseChai:
    def __init__(self , type_):
        self.type_ = type_

    def prepare(self):
        print(f"Preparing {self.type_} chai")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding spices...")
    
    # inheritance

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")
        # this is basically like doing BaseChai("Regular")
        # So now self.chai is an instance of BaseChai
    
    def serve(self):
        print(f"Serving {self.chai.type_} chai" )
        self.chai.prepare()


class Fancy(ChaiShop):
    chai_cls = MasalaChai

masala = MasalaChai("Regular")
# MasalaChai doesnt have a constructor of its own
# its inheriting BaseChai so its using the constructor of that class
# that constructor needs type_ , therefore we need to send "Regular"
masala.add_spices()
masala.prepare()

shop = ChaiShop()
shop.chai.prepare()
shop.serve()

fancy = Fancy()
fancy.chai.prepare()
# fancy.chai_cls.prepare()
# fancy.chai_cls.add_spices()
# fancy.chai_cls.prepare wont work but fancy.chai.prepare() works , why so?
# because chai_cls is basically BaseChai
# so we are basically calling BaseChai.prepare() , and we need a reference if we call by class
# thats why we get an error
# same situation is explained for line 62 and 63 
# same reason for fancy.chai_cls.add_spices()

fancy.serve()


class A:
    def __init__(self , name , age):
        self.name = name
        self.age = age

class B(A):
    def __init__(self, name, age , roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

# super() = reuse parent class code instead of rewriting it

# class C(A , B):
    # here suppose class A and B has same method
    # method named function()
    # and if we make an object of C and call function()
    # which will be called? A class function() or B class function()
    # A class will be called because it is written first -> A,B.



# class Utils():
    
#     def raw():
#         print("This is raw")

# obj = Utils()
# obj.raw()
# instead of this we can do this by making raw a static method


class Utils():
    
    @staticmethod
    def raw():
        print("This is raw")

Utils.raw()
# static methods are not dependent on objects
# with static methods u do not need self to pass in functions.

# class methods

class Random:

    def __init__(self , size):
        self.size = size
    
    @classmethod
    def randomA(cls , size):
        
        return cls(
            size['regular'],
            size['medium'],
            size['small']
        )
    
    @classmethod
    def randomB(cls , size):
       
        return cls(
            regular , small = size
        )
class Random:

    def __init__(self, regular, medium, small):
        self.regular = regular
        self.medium = medium
        self.small = small

    @classmethod
    def from_dict(cls, size):
        # we write for size expecting it to a dictionary
        return cls(
            size['regular'],
            size['medium'],
            size['small']
        )

    @classmethod
    def from_tuple(cls, size):
         # we will write for size expecting it to a tuple
        return cls(*size)


size_dict = {
    'regular': '34',
    'medium': '32',
    'small': '30'
}

size_tuple = (34, 32, 30)

a = Random.from_dict(size_dict)
b = Random.from_tuple(size_tuple)

print(a.__dict__)
print(b.__dict__)



# Why use class methods?
# 1. Alternative constructors

# Your __init__ expects a certain format (in your case, size). But sometimes your data comes in different forms (like a dictionary or tuple).

# Instead of forcing the user to convert data manually, you provide different constructors:

# @classmethod
# def randomA(cls, size_dict):
#     return cls(size_dict['regular'])

# So instead of:

# Random(size_dict['regular'])

# You can do:

# Random.randomA(size_dict)

# 👉 Much cleaner and more flexible.

# 2. They use cls instead of self
# self → instance (object)
# cls → class itself

# This means:

# return cls(...)

# will create a new object of the class, not just call a function.

