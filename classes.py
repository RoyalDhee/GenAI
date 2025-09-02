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
class Student:
    def __init__(self, name, course, level):
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False

# Method: Action the student can do

    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"

# Method: Another action

    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course} "
        else:
            return f"{self.name} must pay school fees first!"

# Method Calculates CGPA

    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"


# Using Methods
Oluwadamilare = Student("Oluwadamilare Bello", "Electrical Engineering", 500)

print(Oluwadamilare.pay_school_fees())
print(Oluwadamilare.register_courses())
print(Oluwadamilare.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))
