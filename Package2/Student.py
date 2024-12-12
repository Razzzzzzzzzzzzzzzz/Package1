class Student:
  def __init__(self, ID, name, age):
      if type(ID) != str:
          raise TypeError("ID Must be a string.")
      if len(ID) != 9:
          ID = "000000000"
      if type(name) != str:
          raise TypeError("Name must be a string.")
      if type(age) != int:
          raise TypeError("Age must be an int.")
      if age < 0:
          age = 0
      self.ID = ID
      self.name = name
      self.age = age
      self.subjects = {}


  def __str__(self):
      return f"ID: {self.ID}, Name: {self.name}, Age: {self.age}, Subjects: {self.subjects}"


  def __repr__(self):
      return f"ID: {self.ID}, Name: {self.name}, Age: {self.age}"


  def __eq__(self, other):
      return self.ID == other.ID


  def __gt__(self, other):
      return self.age > other.age


  def add_grade(self, subject, grade):
      if type(subject) != str:
          raise TypeError("Subject must be a string.")
      if type(grade) != int:
          raise TypeError("Grade must be an int.")
      if grade < 0 or grade > 100:
          grade = 0
      self.subjects[subject] = grade


  def calc_factor(self, subject, percent):
      if subject in self.subjects and self.subjects[subject] + self.subjects[subject] * (percent / 100) <= 100:
          self.subjects[subject] += self.subjects[subject] * (percent / 100)
      else:
          self.subjects[subject] = 100


  def average(self):
      if len(self.subjects) == 0:
          raise ValueError("Subjects can't be empty")
      return sum(self.subjects.values()) / len(self.subjects)


if __name__ == "__main__":
  Raz = Student("012", "Barak", 15)
  Raz.add_grade("English", 40)
  Raz.add_grade("Math", 80)
  # Raz.add_grade("English", 90)
  print(Raz)
  Raz.calc_factor("Math", 20)
  print(Raz)
  print(Raz.average())
