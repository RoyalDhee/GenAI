class Student:
    def __init__(self, name, course, level):  # This runs automatically
        print("Creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created!")