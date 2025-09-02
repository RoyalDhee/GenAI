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

# More Example
class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joned {self.network} network")
    
    def buy_airtime(self, amount):
        self.airtime += amount
        return f"{self.name} now has {self.airtime} airtime"
    
Dasola = PhoneUser("Dasola", "MTN")
Tope = PhoneUser("Temitope", 'Airtel')

print(Dasola.buy_airtime(500))
print(Tope.buy_airtime(12500))
print(Tope.airtime)
    

        