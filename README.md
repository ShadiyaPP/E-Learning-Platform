# E-Learning Platform using OOP and Inheritance

## Project Overview

This project is a basic **E-Learning Platform** developed using Python and Object-Oriented Programming (OOP) concepts.

The project demonstrates:

* Classes and objects
* Inheritance
* Constructors
* Encapsulation
* Method creation
* Relationships between objects

The platform contains users, students, instructors, and courses.

---

## Project Structure

```text
E-Learning-Platform/
│
├── E-Learning_Platform.py
└── README.md
```

---

## Classes Used

### 1. User Class

`User` is the parent class.

It contains common information shared by students and instructors:

* Name
* Email
* User ID

```python
class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id
```

---

### 2. Student Class

`Student` inherits from the `User` class.

```python
class Student(User):
```

A student can:

* Enroll in a course
* View enrolled courses
* Check course progress
* Update course progress

Methods implemented:

```text
enroll_course()
view_courses()
check_progress()
update_progress()
```

---

### 3. Instructor Class

`Instructor` also inherits from the `User` class.

```python
class Instructor(User):
```

An instructor can:

* Create courses
* Display the courses they are teaching

Methods implemented:

```text
create_course()
display_courses()
```

---

### 4. Course Class

The `Course` class stores course-related information such as:

* Course ID
* Course name
* Instructor
* Enrolled students

Each course is associated with an instructor who creates it.

---

## Inheritance

Inheritance is demonstrated using the `User` class as the parent class.

```text
              User
             /    \
            /      \
       Student   Instructor
```

Both `Student` and `Instructor` inherit the common attributes and functionality from `User`.

For example:

```python
class Student(User):
```

and

```python
class Instructor(User):
```

The `super()` function is used to initialize the attributes of the parent class.

```python
super().__init__(name, email, user_id)
```

---

## Student Features

### Enroll in a Course

A student can enroll in a course using:

```python
student1.enroll_course(course1)
```

The course is added to the student's enrolled courses.

### View Enrolled Courses

```python
student1.view_courses()
```

This displays all courses in which the student is enrolled.

### Check Course Progress

```python
student1.check_progress(course1)
```

This displays the student's progress percentage for the selected course.

### Update Course Progress

```python
student1.update_progress(course1, 75)
```

This updates the student's course progress to 75%.

---

## Instructor Features

### Create a Course

An instructor can create a course using:

```python
course1 = instructor1.create_course(
    "C001",
    "Python Programming"
)
```

### Display Teaching Courses

An instructor can view the courses they have created:

```python
instructor1.display_courses()
```

---

## Demonstration

The program creates:

### Instructors

1. John
2. Sarah

### Students

1. Alice
2. Bob

### Courses

1. Python Programming
2. Data Science
3. Machine Learning

---

## Sample Operations

The demonstration includes:

```python
student1.enroll_course(course1)
student1.enroll_course(course3)

student2.enroll_course(course1)
student2.enroll_course(course2)
```

Students can then view their enrolled courses:

```python
student1.view_courses()
student2.view_courses()
```

Their course progress can also be checked and updated:

```python
student1.check_progress(course1)

student1.update_progress(course1, 75)

student1.check_progress(course1)
```

The instructors can display the courses they teach:

```python
instructor1.display_courses()
instructor2.display_courses()
```

---

## How to Run the Project

### Step 1: Clone or download the project

Download the project files to your computer.

### Step 2: Open the project folder

Make sure the folder contains:

```text
E-Learning_Platform.py
README.md
```

### Step 3: Run the Python file

Open a terminal in the project folder and run:

```bash
python E-Learning_Platform.py
```

---

## Expected Output

The program will display information similar to:

```text
John created course: Python Programming
John created course: Data Science
Sarah created course: Machine Learning

Alice enrolled in Python Programming
Alice enrolled in Machine Learning

Bob enrolled in Python Programming
Bob enrolled in Data Science

Courses enrolled by Alice:
- C001: Python Programming
- C003: Machine Learning

Courses enrolled by Bob:
- C001: Python Programming
- C002: Data Science

Alice's progress in Python Programming: 0%
Bob's progress in Data Science: 0%

Progress updated to 75% for Python Programming
Progress updated to 50% for Data Science

Alice's progress in Python Programming: 75%
Bob's progress in Data Science: 50%
```

---

## OOP Concepts Demonstrated

| OOP Concept   | Implementation                             |
| ------------- | ------------------------------------------ |
| Class         | `User`, `Student`, `Instructor`, `Course`  |
| Object        | Students, instructors, and courses         |
| Inheritance   | `Student(User)` and `Instructor(User)`     |
| Constructor   | `__init__()`                               |
| Encapsulation | Data stored inside class objects           |
| Method        | `enroll_course()`, `create_course()`, etc. |
| `super()`     | Used to initialize the parent `User` class |

---

## Conclusion

This project demonstrates how Object-Oriented Programming and inheritance can be used to build a simple E-Learning Platform.

The `User` class provides common user information, while `Student` and `Instructor` extend the functionality through inheritance. The `Course` class manages course-related information, allowing students to enroll and track progress while instructors can create and manage their courses.
