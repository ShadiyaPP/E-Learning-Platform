class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id


class Student(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.enrolled_courses = {}

    def enroll_course(self, course):
        self.enrolled_courses[course] = 0
        print(f"{self.name} enrolled in {course.name}.")

    def view_courses(self):
        print(f"\n{self.name}'s Enrolled Courses")

        if not self.enrolled_courses:
            print("No courses enrolled.")
            return

        for course, progress in self.enrolled_courses.items():
            print(f"{course.name} - Progress: {progress}%")

    def check_progress(self, course):
        if course in self.enrolled_courses:
            print(
                f"{self.name}'s progress in "
                f"{course.name}: "
                f"{self.enrolled_courses[course]}%"
            )
        else:
            print(
                f"{self.name} is not enrolled in "
                f"{course.name}."
            )

    def update_progress(self, course, progress):
        if course in self.enrolled_courses:
            self.enrolled_courses[course] = progress


class Instructor(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.courses = []

    def create_course(self, course):
        self.courses.append(course)
        print(
            f"{self.name} created course: "
            f"{course.name}"
        )

    def display_courses(self):
        print(f"\n{self.name}'s Courses")

        if not self.courses:
            print("No courses created.")
            return

        for course in self.courses:
            print(f"- {course.name}")


class Course:
    def __init__(self, course_id, name, category):
        self.course_id = course_id
        self.name = name
        self.category = category


# ---------------------------------------------------------
# Create Instructors
# ---------------------------------------------------------

instructor1 = Instructor(
    "Rahul",
    "rahul@example.com",
    "I001"
)

instructor2 = Instructor(
    "Priya",
    "priya@example.com",
    "I002"
)


# ---------------------------------------------------------
# Create Students
# ---------------------------------------------------------

student1 = Student(
    "Arun",
    "arun@example.com",
    "S001"
)

student2 = Student(
    "Anjali",
    "anjali@example.com",
    "S002"
)


# ---------------------------------------------------------
# Create 3 Courses
# ---------------------------------------------------------

python_course = Course(
    "C001",
    "Python Programming",
    "Programming"
)

data_science = Course(
    "C002",
    "Data Science",
    "Data Science"
)

machine_learning = Course(
    "C003",
    "Machine Learning",
    "AI/ML"
)


# ---------------------------------------------------------
# Instructor Creates Courses
# ---------------------------------------------------------

instructor1.create_course(python_course)
instructor1.create_course(data_science)

instructor2.create_course(machine_learning)


# ---------------------------------------------------------
# Display Instructor Courses
# ---------------------------------------------------------

instructor1.display_courses()
instructor2.display_courses()


# ---------------------------------------------------------
# Student Enrollment
# ---------------------------------------------------------

student1.enroll_course(python_course)
student1.enroll_course(data_science)

student2.enroll_course(data_science)
student2.enroll_course(machine_learning)


# ---------------------------------------------------------
# Update Course Progress
# ---------------------------------------------------------

student1.update_progress(python_course, 75)
student1.update_progress(data_science, 40)

student2.update_progress(data_science, 60)
student2.update_progress(machine_learning, 30)


# ---------------------------------------------------------
# View Enrolled Courses
# ---------------------------------------------------------

student1.view_courses()
student2.view_courses()


# ---------------------------------------------------------
# Check Progress
# ---------------------------------------------------------

print("\n--- Course Progress ---")

student1.check_progress(python_course)
student1.check_progress(data_science)

student2.check_progress(data_science)
student2.check_progress(machine_learning)