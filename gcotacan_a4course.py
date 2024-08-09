import random

courses = []


class Course:
    # class variables
    semester = 'Fall 2025'

    def __init__(self, name='', categories=None):
        """Create a course object. self refers to the object"""
        self.section = random.randint(10000, 100000)
        self.name = name
        self.student_count = 0
        self.class_roster = []
        # Instance variable categories will hold a description and total point value
        if categories is None:
            self.categories = {}
            self.enter_categories()
        else:
            self.categories = categories

    @classmethod
    def change_semester(cls, semester):
        """Modify the text of the semester that all courses are being added to"""
        cls.semester = semester

    def enter_categories(self):
        """Method to accept all categories for a course"""
        print(f'Enter grading categories for {self.name}:')
        while True:
            category_name = input('5 letter max Category name: ').strip()
            total_points = int(input(f'Enter total points for that {category_name}: '))
            self.categories[category_name] = total_points
            more_categories = input('Do you have more categories to enter (Y/N): ').strip().lower()
            if more_categories != 'y':
                break

    def enroll_students(self, number):
        """Method to enroll students in course"""
        self.student_count += number
        for _ in range(number):
            student = Student(self.categories)  # Pass categories to Student constructor
            student.fullname = input('Enter student first and last name: ').strip()
            student.enter_scores()
            self.class_roster.append(student)

    def __str__(self):
        """Override __str__ method for course to print roster and scores"""
        result = f'Course {self.section} - {self.name} has {self.student_count} students:\n'
        for student in self.class_roster:
            result += f'{student}\n'
        return result


class Student:
    def __init__(self, categories, fname='Jane', lname='Doe'):
        self.first = fname
        self.last = lname
        self.scores = {category: 0 for category in categories}
        self.total_points = categories  # Add total_points attribute

    @property
    def fullname(self):
        return f'{self.last}, {self.first}'

    @fullname.setter
    def fullname(self, name):
        try:
            self.first, self.last = name.split()
        except ValueError:
            print("Invalid name format. Defaulting to 'Jane Doe'.")

    def enter_scores(self):
        """Method to enter earned points for each grading category"""
        for category in self.scores:
            self.scores[category] = int(input(f'Enter earned points for {category}: '))

    def __str__(self):
        result = f'{self.fullname} - '
        for category, score in self.scores.items():
            total_points = self.total_points.get(category, 0)  # Retrieve total points for category
            result += f'{category}: {score}/{total_points}, '  # Display score/total points
        return result.rstrip(', ')


# Main Logic
print(f"{'University System':*^30}")
Course.change_semester(input('Enter semester and year for which you are creating courses: '))

enter_courses = 'y'
print("\nEntering course information")
while enter_courses == 'y':
    course_name = input('Enter course name: ').upper()
    new_course = Course(course_name)
    courses.append(new_course)
    enter_courses = input("\nAdd another course (Y/N)? ").casefold()

print('\nAdding students to courses')
for course in courses:
    print(f'\nAdding students to {course.name} course')
    num_students = int(input('How many students do you want to enroll? '))
    course.enroll_students(num_students)

print(f'\nCourse Information for {Course.semester}')
for course in courses:
    print(course)


