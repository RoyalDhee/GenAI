# class Student:
#     def __init__(self, name, course, level):  # This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created!")
#         print(f"He is in {level} level, {course} department")

# mayowa = Student("Mayowa Adeagbo", "Mechatronics Engineering", 500)

# # How Init and Self work together
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Creating Student object...")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"{self.name} from {self.state_of_origin} is ready!")


#     def generate_id(self):
#         import random
#         return f"UNISAIL {random.randint(1000, 9999)}"


# shola = NigerianStudent("Shola John", "Ogun State", "Physics")
# print(shola.student_id)

# # More Example
# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joned {self.network} network")

#     def buy_airtime(self, amount):
#         self.airtime += amount
#         return f"{self.name} now has {self.airtime} airtime"

# Dasola = PhoneUser("Dasola", "MTN")
# Tope = PhoneUser("Temitope", 'Airtel')

# print(Dasola.buy_airtime(500))
# print(Tope.buy_airtime(12500))
# print(Tope.airtime)

# Defining Attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0


# Ayomide = Student("Ayomide Bello", "Linguistics", 100, "Ogun State")

# print(Ayomide.name)
# print(Ayomide.level)
# print(Ayomide.course)
# print(Ayomide.state_of_origin)

# Types of Attributes
# Instance Attributes - unique to each objects
# student1 = Student("John Paul", "Hospitality", 500, "Ebonyi State")
# student2 = Student("Abel King", "Management", 500, "Anambra State")

# print(student1.name)
# print(student2.course)

# # Class Attributes
# class Student:
#     university = "Federal University of Agriculture Abeokuta"

#     def __init__(self, name, course):
#         self.name = name
#         self.course = course

# print(Student.university)
# print(student1.university)
# print(student2.university)

# Methods: they define actions object can perform. they are like a function
# class Student:
#     def __init__(self, name, course, level):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False

# # Method: Action the student can do

#     def pay_school_fees(self):
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"

# # Method: Another action

#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course} "
#         else:
#             return f"{self.name} must pay school fees first!"

# # Method Calculates CGPA

#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"

#     def academic_calender(self):
#         return f"Academic calender runs from spetember to July"


# # Using Methods
# Oluwadamilare = Student("Oluwadamilare Bello", "Electrical Engineering", 500)

# print(Oluwadamilare.pay_school_fees())
# print(Oluwadamilare.register_courses())
# print(Oluwadamilare.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))


# class BankAccount:
#     def __init__(self, owner, bank_name, balance=0):
#         # Attributes that the account has
#         self.owner = owner
#         self.bank_name = bank_name
#         self.balance = balance
#         self.account_number = self.generate_account_number()

# Method - What the account can do
#     def deposit(self, amount):
#         """"Add money to the account"""
#         if amount > 0:
#             self.balance += amount  # Method changes attribute
#             return f"₦{amount:} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance}"
#         return f"Invalid deposit amount"

#     def withdraw(self, amount):
#         """Remove money from the account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"₦{amount:} has been withdrawn from {self.owner}'s account. New balance: ₦{self.balance}"
#         return f"Invalid amount or Inssufecient fund"

#     def transfer(self, amount):
#         """Transfer money from account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"₦{amount:} has been transferred from {self.owner}'s acoount. New balance: ₦{self.balance}"
#         return "Transfer failed: Insuffecient funds"

#     def check_balance(self):
#         """Check Balance"""
#         return f"{self.owner}'s {self.bank_name} account balance is ₦{self.balance:}"

#     def generate_account_number(self):
#         """Generate a unique account number """
#         import random
#         return f"01{random.randint(10000000, 99999999)}"


# # Creating and using the element
# ayomide_account = BankAccount("Ayomide Bello", "Wema Bank", 60000)

# print(f"owner: {ayomide_account.owner}")
# print(f"Bank: {ayomide_account.bank_name}")
# print(f"Account Number: {ayomide_account.account_number}")


# print(ayomide_account.deposit(50000))
# print(ayomide_account.withdraw(10000))
# print(ayomide_account.transfer(2000))
# print(ayomide_account.check_balance())

# Practice Exercise
# class NaijaPhone:
#     def __init__(self, name, brand, model, network_provider):
#         self.name = name
#         self.brand = brand
#         self.model = model
#         self.network_provider = network_provider
#         self.airtime_balance = 0
#         self.data_balance = 0
#         self.is_on = False

#     def power_on(self):
#         self.is_on = True
#         return f"{self.name} {self.brand} is now on. Network: {self.network_provider}"
    
#     def buy_airtime(self, amount):
#         self.airtime_balance += amount
#         return f"₦{amount} airtime purchased. Balance is ₦{self.airtime_balance}"

#     def make_call(self, number):
#         if self.is_on and self.airtime_balance > 0:
#             self.airtime_balance -= 10
#             return f"Calling {number} .... Remaining airtime: ₦{self.airtime_balance}"
#         return "Cannot make call. Check phone power and airtime"

#     def send_sms(self, message, number):
#         if self.airtime_balance >= 4:
#             self.airtime_balance -=4
#             return f"Sms sent to {number}: '{message}'. Remaining airtine: ₦{self.airtime_balance}"
#         return f"Insuffecient airtime to send SMS"

# gabriel = NaijaPhone("Gabby's", "iPhone", "15 pro max", "MTN")

# print(f"Brand of phone {gabriel.brand}")
# print(f"Model: {gabriel.model}")
# print(f"Network: {gabriel.network_provider}")

# print(gabriel.power_on())
# print(gabriel.buy_airtime(2000))
# print(gabriel.make_call(7066195239))

# Practice Exercise 2
# class BRTBus:
#     def __init__(self, route, bus_number):
#         self.route = route
#         self.bus_number = bus_number
#         self.current_stop = "Ikorodu"
#         self.passenger_count = 0
#         self.fare = 500

#     def announce_stop(self):
#         return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"

#     def board_passengers(self, count):
#         self.passenger_count -= count
#         return f"{count} passengeers boarded. Total: {self.passenger_count}"
# Brt1 = BRTBus("Oshodi-Ikorodu", 373)

# print(Brt1.route)
# print(Brt1.announce_stop())

# Practice excercise 3
# class MarketTrader:
#     def __init__(self, name, market_name, goods):
       
#         self.name = name                
#         self.market_name = market_name 
#         self.goods = goods             
#         self.daily_sales = 0
    
  
#     def advertise_goods(self):
#         return f"{self.name} at {self.market_name}: Fresh {', '.join(self.goods)} available!"
    
#     def make_sale(self, amount):
#         self.daily_sales += amount
#         return f"Sale made! Today's total: ₦{self.daily_sales:,}"

# Encapsulation
class NigerianBankAccount:
    def __init__(self, owner, inintial_balance=0):
        self.owner = owner
        self._balance = inintial_balance #protected attribute
        self.__pin = "1234" #Private attribute
        self._transaction_history = [] #Protected attribute

    # Public methods - anyone can use these
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited ₦{amount}")
            return f"₦{amount} deposited successfully"
        return f"Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):  # Uses private method
            if amount <= self._balance:
                self._balance -= amount
                self._transaction_history.append(f"Withdrew ₦{amount:,}")
                return f"₦{amount:,} withdrawn successfully"
            return "Insufficient funds"
        return "Invalid PIN"
    
    def check_balance(self, pin):
        if self.__verify_pin(pin):
            return f"Current balance: ₦{self._balance:,}"
        return "Invalid PIN"

    # Private method - only the class can use this
    def __verify_pin(self, entered_pin):
        return entered_pin == self.__pin
    
    # Protected method - subclasses can use this
    def _get_transaction_history(self):
        return self._transaction_history.copy()
    
# Using the encapsulated account
gbenga_account = NigerianBankAccount("Gbenga Folarin", 20000)

print(gbenga_account.deposit(100000))
print(gbenga_account.withdraw(2000, "1234"))
print(gbenga_account.check_balance("1234"))

print(gbenga_account.__pin("1234"))
gbenga_account.__pin

# Abstraction
from abc import ABC, abstractmethod

# Abstract base class - defines what a Nigerian student should do
class NigerianStudent(ABC):
    def __init__(self, name, course, level):
        self.name = name
        self.course = course
        self.level = level
        self.fees_paid = False

    # Concrete method - all students can do this
    def pay_school_fees(self, amount):
        self.fees_paid = True
        return f""

