# Parent Class
class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")


# Course Class
class Course:
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.students = []

    def display_course(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Instructor: {self.instructor.name}")


# Student inherits from User
class Student(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.enrolled_courses = {}

    # Student can enroll in a course
    def enroll_course(self, course):
        if course.course_id not in self.enrolled_courses:
            self.enrolled_courses[course.course_id] = 0
            course.students.append(self)
            print(f"{self.name} enrolled in {course.course_name}")
        else:
            print(f"{self.name} is already enrolled in {course.course_name}")

    # Student can view enrolled courses
    def view_courses(self):
        print(f"\nCourses enrolled by {self.name}:")

        if not self.enrolled_courses:
            print("No courses enrolled.")
            return

        for course_id in self.enrolled_courses:
            print(f"- {course_id}: {courses[course_id].course_name}")

    # Student can check course progress
    def check_progress(self, course):
        if course.course_id in self.enrolled_courses:
            progress = self.enrolled_courses[course.course_id]
            print(
                f"{self.name}'s progress in "
                f"{course.course_name}: {progress}%"
            )
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")

    # Optional method to update progress
    def update_progress(self, course, progress):
        if course.course_id in self.enrolled_courses:
            if 0 <= progress <= 100:
                self.enrolled_courses[course.course_id] = progress
                print(
                    f"Progress updated to {progress}% "
                    f"for {course.course_name}"
                )
            else:
                print("Progress must be between 0 and 100.")
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")


# Instructor inherits from User
class Instructor(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.teaching_courses = []

    # Instructor can create courses
    def create_course(self, course_id, course_name):
        course = Course(course_id, course_name, self)
        self.teaching_courses.append(course)

        print(
            f"{self.name} created course: "
            f"{course_name}"
        )

        return course

    # Instructor can display courses they teach
    def display_courses(self):
        print(f"\nCourses taught by {self.name}:")

        if not self.teaching_courses:
            print("No courses created.")
            return

        for course in self.teaching_courses:
            print(
                f"- {course.course_id}: "
                f"{course.course_name}"
            )


# --------------------------------------------------
# DEMONSTRATION
# --------------------------------------------------

# Create 2 instructors
instructor1 = Instructor(
    "John",
    "john@example.com",
    "I001"
)

instructor2 = Instructor(
    "Sarah",
    "sarah@example.com",
    "I002"
)


# Create 3 courses
course1 = instructor1.create_course(
    "C001",
    "Python Programming"
)

course2 = instructor1.create_course(
    "C002",
    "Data Science"
)

course3 = instructor2.create_course(
    "C003",
    "Machine Learning"
)


# Create 2 students
student1 = Student(
    "Alice",
    "alice@example.com",
    "S001"
)

student2 = Student(
    "Bob",
    "bob@example.com",
    "S002"
)


# Student enrollment
student1.enroll_course(course1)
student1.enroll_course(course3)

student2.enroll_course(course1)
student2.enroll_course(course2)


# View enrolled courses
student1.view_courses()
student2.view_courses()


# Check progress
student1.check_progress(course1)
student2.check_progress(course2)


# Update progress
student1.update_progress(course1, 75)
student2.update_progress(course2, 50)


# Check updated progress
student1.check_progress(course1)
student2.check_progress(course2)


# Display instructor courses
instructor1.display_courses()
instructor2.display_courses()


# Display course information
print("\nCourse Details:")
course1.display_course()
course2.display_course()
course3.display_course()