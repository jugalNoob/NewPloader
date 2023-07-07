i = 1
while i < 6:
  print(i)
  i += 1

  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


  for x in range(6):
   print(x)


   #|||||||||||Creating a Function||||||||||||||||||

def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


#Python Inheritance||||


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)



# |"||||||||||||||||||||function Local Scope




x = 300
def myinnerfunc():
    print(x)
myinnerfunc()

myfunc()


import datetime

x = datetime.datetime.now()
print(x)


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

print(x)


#Built-in Math Functions||||||||||||||||||||||||

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)
import math

x = math.sqrt(64)

print(x)


x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

x = math.pi

print(x)

username = input("Enter username:")
print("Username is: " + username)