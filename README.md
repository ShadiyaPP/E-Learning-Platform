# 🎓 E-Learning Platform

## 📌 Overview

A basic **E-Learning Platform** implemented using **Python Object-Oriented Programming (OOP)** and **inheritance**.

The system models users, students, instructors, and courses with functionality for course creation, student enrollment, course tracking, and progress monitoring.

## 🛠️ Tech Stack

* 🐍 **Python 3**
* 🧩 **Object-Oriented Programming**
* 🔗 **Inheritance**
* 📦 **No external dependencies**
* 💻 **Console-based application**

## 🏗️ Class Architecture

```text
                    👤 User
                   /       \
                  /         \
          🎓 Student     👨‍🏫 Instructor
              |               |
              |               └── Create Courses
              |               └── Display Courses
              |
              ├── Enroll in Courses
              ├── View Enrolled Courses
              └── Check Course Progress

                    📚 Course
```

## 👤 `User` Class

Parent class containing common user attributes.

**Attributes:**

```text
name
email
user_id
```

Both `Student` and `Instructor` inherit these attributes using:

```python
super().__init__()
```

## 🎓 `Student` Class

Child class derived from `User`.

**Methods:**

* `enroll_course()` – Enroll in a course
* `view_courses()` – Display enrolled courses and progress
* `check_progress()` – Check progress for a specific course
* `update_progress()` – Update course completion percentage

## 👨‍🏫 `Instructor` Class

Child class derived from `User`.

**Methods:**

* `create_course()` – Create and assign courses
* `display_courses()` – Display courses created by the instructor

## 📚 `Course` Class

Represents an individual course.

**Attributes:**

```text
course_id
name
category
```

## 📊 Test Data

### 👨‍🏫 Instructors

* Rahul
* Priya

### 🎓 Students

* Arun
* Anjali

### 📚 Courses

* Python Programming
* Data Science
* Machine Learning

## 🔄 Application Flow

```text
👤 Create Users
       ↓
👨‍🏫 Create Instructors
       ↓
📚 Create Courses
       ↓
➕ Instructors Create Courses
       ↓
🎓 Students Enroll
       ↓
📋 View Enrolled Courses
       ↓
📈 Update Progress
       ↓
📊 Check Course Progress
```

## 🧠 OOP Concepts Demonstrated

* 🧱 Classes & Objects
* 🔗 Inheritance
* 🔧 Constructors
* `super()`
* 📦 Instance Attributes
* ⚙️ Instance Methods
* 🤝 Object Interaction
* 🔒 Encapsulation

## 📂 Project Structure

```text
E-Learning-Platform/
│
├── E-Learning_Platform.py
└── README.md
```

## 🚀 How to Run

### 1️⃣ Verify Python

```bash
python --version
```

### 2️⃣ Run the Application

```bash
python E-Learning_Platform.py
```

## ✅ Expected Functionality

The application demonstrates:

* 👨‍🏫 2 instructors
* 🎓 2 students
* 📚 3 courses
* ➕ Instructor course creation
* 📝 Student course enrollment
* 📋 Enrolled course listing
* 📈 Course progress tracking
* 🔗 Inheritance between `User`, `Student`, and `Instructor`

## 🔮 Future Enhancements

* 🔐 User authentication
* 🗄️ Database integration
* 📹 Video course content
* 📝 Quizzes and assessments
* 🏆 Certificates
* 📊 Instructor analytics
* 🌐 Web interface
* 💳 Course payment system


