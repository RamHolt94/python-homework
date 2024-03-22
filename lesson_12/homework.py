# Homework: Classes
# Read carefully until the end before you start solving the exercises.

# Practice the Basics

# Basic Class

# - Create an empty class HouseForSale
# - Create two instances.
# - Add number_of_rooms and price as instance attributes.
# - Create print statements that show the attribute values for the instances.
class HouseForSale:
    pass
number_of_rooms = HouseForSale()
price = HouseForSale()
print(number_of_rooms)
print(price)
# ----------------------------------------------------------------------------------------------------------------------

# Instance Methods

# - Create a Computer class.
# - Create method:
#   - turn_on that prints Computer has Turned On
#   - turn_off that prints Computer has Turned Off
# - Create an instance of the Computer class then call each method.
class Computer:
    pass
    def turn_on(self):
        print("Computer has Turned On")
    def turn_off(self):
        print("Computer has Turned Off")
p_c = Computer()
p_c.turn_on()
p_c.turn_off()
# ----------------------------------------------------------------------------------------------------------------------

# Constructor with Parameters

# - Create a Dog class.
# - Dog should have a constructor with a name parameter.
# - Dog should have a method say_name that prints the name of the dog.
class Dog:
    pass
    def __init__(self, name):
        self.name = name
    def say_name(self, name):
        print(f"The dogs name is {self.name}")
pup = Dog(name="Grey")
pup.say_name("Grey")

# ----------------------------------------------------------------------------------------------------------------------

# Inheritance

# Create the classes that would make the following code possible, with the caveat that
# both Dog and Cat must inherit from Animal.
class Animal:
    def __init__(self, name):
        self.name = name
    def say_name(self, name):
        print(self.name)
    def speak(self):
        print("Prints: I can't speak!")
animal = Animal("I don't have a name yet.")
animal.say_name("I don't have a name yet.")   # Prints: I don't have a name yet.
animal.speak()      # Prints: I can't speak!
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Prints: Woof!")
dog = Dog('Fido')
dog.say_name('Fido')      # Prints: Fido
dog.speak()         # Prints: Woof!
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Prints: Meow!")
cat = Cat('Max')
cat.say_name('Max')      # Prints: Max
cat.speak()         # Prints: Meow!

# ----------------------------------------------------------------------------------------------------------------------

# Exercises
# Exercise 1: Books and Authors

# Create an empty class called Book. Then create three instances.
# Add the following attributes for each of the instances: title, author, and publication_year.
# Create print statements to display the attributes of each one of the instances.

# Pre-code:
class Book:
   pass

book1 = Book()
book1.title = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.publication_year = 1960

# Your code here
def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year


# def title(self, title):
#         self.title = title
#         print("To kill a Mockingbird")
# def author(self, author):
#         self.author = author
#         print("Harper")
#
# def publication_year(self):
#         self.publication_year = publication_year()
#         print(1960)
print("Title:", book1.title)
print("Author:", book1.author)
print("Publication Year:", book1.publication_year)


# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Vehicle and Types of Vehicles

# Create a Vehicle class.
# - Its constructor should take the name and type of the vehicle and store them as instance attributes.
# - This Vehicle class should also have a show_type() instance method that prints out the
#   message: "<NAME_OF_VEHICLE> is a <TYPE_OF_VEHICLE>"
# - Create Car and Bike classes that inherit from Vehicle.
# - Create instances of Car and Bike and make them show their types.
class Vehicle:
    def __init__(self, name, vehicle_type):
        self.name = name
        self.vehicle_type = vehicle_type

    def show_type(self):
            print(f"{self.name} is a {self.vehicle_type}")
class Car(Vehicle):
    pass

    def __init__(self, name):
        super().__init__(name, "Car")

class Bike(Vehicle):
    pass

    def __init__(self, name):
        super().__init__(name, "Bike")

car = Car("Camry")
car.show_type()
bike = Bike("Street Racing")
bike.show_type()
# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Spot and correct the mistakes

# - You are given a task to create a Car class.
# - Each car will have attributes for model and year.
# - Unfortunately, the given code below contains several mistakes.
# - Your task is to find and correct these mistakes to make the code run successfully.
# - Please include a comment in the code explaining the corrections you made and why.

# Pre-code
class Car:
   def __init__(self, model, year): # this constructor is missing the 'self' parameter so I added it.
       self.model = model #fixed the attributes by adding "self" at the begining.
       self.year = year
   def my_car(self, model, year):  #created the instance
        __init__(model,year) # created the method
my_car = Car("Toyota", "1997") # added the year
print(my_car.model)
print(my_car.year)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. SmartHome with Constructor

# Create a SmartHome class that has a constructor __init__ and a send_notification() method.
#
# The constructor should initialize the attributes:
# - home_name
# - location
# - number_of_devices
#
# send_notification() should print a notification including the home_name and location.

# Create instances for the following:
# Home Name      Location      Number of Devices
# Villa Rosa     New York      15 devices
# Green House    California    10 devices
# Sea View       Florida       20 devices

# Call the send_notification() method for each instance,
# passing a message reminding to turn off the lights.
class SmartHome:
    def __init__(self, home_name, location, number_of_devices):
        self.home_name = home_name
        self.location = location
        self.number_of_devices = number_of_devices
    def send_notification(self):
        print(f"Home: {self.home_name} and Location: {self.location}, don't forget to turn off the lights!")
    # def number_of_devices(self, number_of_devices):
    #         __init__(number_of_devices)
home1 = SmartHome("Villa Rosa","New York","15 devices")
home2 = SmartHome("Green House", "California","10 devices")
home3 = SmartHome("Sea View", "Florida","20 devices")

home1.send_notification()
home2.send_notification()
home3.send_notification()
# ----------------------------------------------------------------------------------------------------------------------

# Exercise 5. Inheritance. Spot and correct mistakes

# You should have the following hierarchy of classes:

 # Animal
 # │
 # ├── Mammal
 # │
 # ├── Bird
 # │
 # └── Fish

# Each class has the following attributes:

# - Animal name
# - Mammal name, age, number of legs
# - Bird name, age, can fly or not
# - Fish name, age, number of fins

# But, the provided code for these classes and their instances has several mistakes
# related to hierarchy, class attributes, and instance creation.

# Find and correct these mistakes to make the code work properly.
# Leave a comment in the code explaining what the problems were and why it wouldn't work.
# There are seven mistakes in the pre-code.

# Pre-code
class Animal:
    def __init__(self, name): #removed "age" because the requirements didn't ask for it
        self.name = name      #added self becuase the attribute would be able to be called
        # age = age              #removed this attribute per the requirements

class Mammal(Animal): #removed the "s" from "animals" to allow it to align with the original class
    def __init__(self, name, age, num_legs):
        super().__init__(name) #removed "age" as it would be pulled from the parent class
        self.age = age              #created the attribute for age
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, age, can_fly): #added "name" and "age" here
        super().__init__(name) #created this to pull from the parent class
        self.age = age     #created this attribute
        self.can_fly = can_fly

class Fish(Animal):   #removed "mamal" and added "animal" becasue the hierarchy doesn't line up to the requirments
    def __init__(self, name, age, num_fins):
        super().__init__(name) # removed age because the parent class doesn't have it to pull from
        self.age = age     # added this "age attribute
        self.num_fins = num_fins

tiger = Mammal('Tiger', 5, 4)
sparrow = Bird("Chip", 7, True)         #corrected the arguments here so that the attributes held values
goldfish = Fish('Goldfish', 2, 'Many')

print("Name:", tiger.name, "Age:", tiger.age, "Legs:", tiger.num_legs)
print("Name:", sparrow.name, "Age:", sparrow.age, "Can they fly:", sparrow.can_fly)
print("Name:", goldfish.name, "Age:", goldfish.age, "Number of fins:", goldfish.num_fins)