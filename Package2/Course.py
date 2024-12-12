from os import remove
from Student import Student

class Course:
    def __init__(self, number, name, max_students):
        self.number = number
        self.name = name
        self.max_students = max_students
        self.subjects = {}
        self.students = []

    def __str__(self):
        return (f"Course Number: {self.number}, Course Name: {self.name}, Course Subjects And Teachers: {self.subjects}\n"
                f"Course Students: {self.students}, Max Students: {self.max_students}")

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def add_factor(self, subject, percent):
        for student in self.students:
            student.calc_factor(subject, percent)

    def del_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("Student is not in the course.")

    def averages(self):
        average = {}
        for student in self.students:
            if student.average() < 0:
                average[student.ID] = 0
            else:
                average[student.ID] = student.average()
        return average

    def weak_student(self):
        students_averages = self.averages()
        if not students_averages:
            raise ValueError("Can't calculate weak students for no students.")
        min_grade = min(students_averages.values())
        min_students = []
        for _id in students_averages:
            if students_averages[_id] == min_grade:
                min_students.append(_id)
        return min_students


if __name__ == "__main__":
    My_Course = Course(1,"Python", 3)
    print(My_Course)

    print("----- [Create Students]-----")
    Raz = Student("31525253", "Raz", 15)
    Raz.add_grade("Python", 40)
    Raz.add_grade("Math", 80)
    print(Raz)
    Aviel = Student("64365426", "Aviel", 17)
    Aviel.add_grade("Python", 50)
    Aviel.add_grade("English", 60)
    print(Aviel)
    Dani = Student("2897542", "Dani", 52)
    Dani.add_grade("Python", 50)
    Dani.add_grade("English", 60)
    print(Dani)

    print("----- [Course Print]-----")
    print(My_Course.add_student(Raz))
    print(My_Course.add_student(Aviel))
    My_Course.add_student(Dani)
    print(My_Course.add_student(Raz))
    print(My_Course)

    print("-----[Add Factor]-----")
    My_Course.add_factor("Python", 5)
    print(My_Course.students)

    print("-----[Delete Student]-----")
    print(My_Course.students)
    My_Course.del_student(Aviel)
    print(My_Course.students)

    print("-----[Averages]-----")
    My_Course.add_student(Aviel)
    print(My_Course.averages())

    print(min(My_Course.averages().values()))

    print("-----[Weak Students]-----")
    print(My_Course.weak_student())