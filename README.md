# Course Management System

## Overview

This Python-based Course Management System is designed to simulate the management of university courses. It allows users to create courses, enroll students, and manage student grades across various categories. The system demonstrates fundamental object-oriented programming (OOP) principles and offers a hands-on approach to managing data in an educational context.

## Project Goals

The main objective of this project was to create a scalable and flexible course management system that can be easily adapted to different educational settings. This project also serves as a demonstration of my ability to work with OOP concepts, data structures, and user input handling in Python.

## Key Features

- **Object-Oriented Design**: The system is built using OOP principles, with `Course` and `Student` classes encapsulating the relevant attributes and behaviors.
- **Dynamic Course Creation**: Courses can be created with unique sections and customizable grading categories, showcasing the system’s flexibility.
- **Student Enrollment and Score Management**: The system allows for enrolling students in courses, entering their grades, and dynamically generating a detailed course roster.
- **Semester Management**: Easily update and manage the semester information for all courses at once.
- **User Interaction**: The program uses console input to interact with users, demonstrating proficiency in handling user input and data validation.

## Technologies Used

- **Python 3.x**: The project is implemented entirely in Python, utilizing built-in libraries such as `random` for generating unique course sections.
- **OOP Concepts**: The project emphasizes the use of classes, methods, and properties to model real-world entities and their interactions.

## Implementation Details

The project is structured around two primary classes:

1. **Course**: Manages course-specific data, including the course name, section, enrolled students, and grading categories.
2. **Student**: Represents individual students and their scores in each course.

The program begins by asking the user to input the semester and year, followed by entering details for each course and enrolling students. It then displays a summary of the course, including student names and their grades.

## Relevance to Software Engineering Roles

This project aligns with roles that require a strong understanding of software design, particularly in backend development and data management. The focus on OOP principles and data handling demonstrates key skills relevant to software engineering positions, such as:

- **Backend Development**: The project simulates backend logic for managing course data and student information, which is applicable to many web and software development roles.
- **Data Handling**: The program manages and processes user input, which is a fundamental skill in any data-centric role.
- **Scalable Design**: The system is designed to be easily extendable, making it relevant for positions that require designing scalable and maintainable codebases.

## How to Use

1. **Clone the Repository**: Download or clone this repository to your local machine.
2. **Run the Program**: Execute the Python script in your terminal or command prompt.
3. **Follow the Prompts**: Input the requested data (e.g., semester, course name, student names, and scores).
4. **View Course Details**: The program will display a summary of the course and student data entered.

## Future Enhancements

- **Database Integration**: Implement a database to store course and student data persistently.
- **GUI Interface**: Develop a graphical user interface for easier interaction.
- **Advanced Grading Features**: Introduce weighted grading categories and GPA calculations.

## License

This project is licensed under the MIT License.
