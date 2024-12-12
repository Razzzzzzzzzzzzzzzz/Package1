from email.mime.text import MIMEText

from Student import Student
from Course import Course

Course_Number = int(input("Course Number: "))
Course_Name = input("Course Name: ")
Course_Max_Students = int(input("Course Max Students: "))
My_Course = Course(Course_Number, Course_Name, Course_Max_Students)
My_Course.subjects["Python"] = "Orly"
My_Course.subjects["Math"] = "Michel"
My_Course.subjects["English"] = "Alon"

while len(My_Course.students) < My_Course.max_students:
    user_id = int(input("Enter Student ID: "))
    if user_id != 0:
        user_name = input("Enter Student Name: ")
        user_age = int(input("Enter Student Age: "))
        python_grade = input("Enter Student grade in Python: ")
        math_grade = input("Enter Student grade in Math: ")
        english_grade = input("Enter Student grade in English: ")
        new_student = Student(user_id, user_name, user_age)
        new_student.add_grade("Python", python_grade)
        new_student.add_grade("Math", math_grade)
        new_student.add_grade("English", english_grade)
        if not My_Course.add_student(new_student):
            break
    else:
        break

course_name = input("Enter Course Name: ")
course_percent = int(input("Enter Percentage: "))
My_Course.add_factor(Course_Name, course_percent)

while id in range(len(My_Course.students)):
    for i in My_Course.weak_student():
        if My_Course.students[id].ID == i:
            My_Course.del_student(id)
            break

max_age = My_Course.students[0]
for student in My_Course.students:
    if student.age > max_age.age:
        max_age = student
print(max_age)

print(My_Course)
from email.mime.text import MIMEText


from Student import Student
from Course import Course


Course_Number = int(input("Course Number: "))
Course_Name = input("Course Name: ")
Course_Max_Students = int(input("Course Max Students: "))
My_Course = Course(Course_Number, Course_Name, Course_Max_Students)
My_Course.subjects["Python"] = "Orly"
My_Course.subjects["Math"] = "Michel"
My_Course.subjects["English"] = "Alon"


while len(My_Course.students) < My_Course.max_students:
   user_id = int(input("Enter Student ID: "))
   if user_id != 0:
       user_name = input("Enter Student Name: ")
       user_age = int(input("Enter Student Age: "))
       python_grade = input("Enter Student grade in Python: ")
       math_grade = input("Enter Student grade in Math: ")
       english_grade = input("Enter Student grade in English: ")
       new_student = Student(user_id, user_name, user_age)
       new_student.add_grade("Python", python_grade)
       new_student.add_grade("Math", math_grade)
       new_student.add_grade("English", english_grade)
       if not My_Course.add_student(new_student):
           break
   else:
       break


course_name = input("Enter Course Name: ")
course_percent = int(input("Enter Percentage: "))
My_Course.add_factor(Course_Name, course_percent)


while id in range(len(My_Course.students)):
   for i in My_Course.weak_student():
       if My_Course.students[id].ID == i:
           My_Course.del_student(id)
           break


max_age = My_Course.students[0]
for student in My_Course.students:
   if student.age > max_age.age:
       max_age = student
print(max_age)


print(My_Course)