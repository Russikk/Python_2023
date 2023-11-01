# Щось типу реєстрації на якомусь сайті університету, де можна зареєструватися як студент, викладач або вступник.

class People:
    name = None
    surname = None

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        print("Створення нового об'єкта: ")
        print("name: ", self.name, ". surname: ", self.surname, sep='')

class Student(People):
    faculty = None
    specialty = None

    def __init__(self, name, surname, faculty, specialty):
        super().__init__(name, surname)
        self.faculty = faculty
        self.specialty = specialty

    def __repr__(self):
        return f"Student(name='{self.name}', surname='{self.surname}', faculty='{self.faculty}', specialty='{self.specialty}')"

class Teacher(People):
    subject = None

    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.subject = subject

    def __repr__(self):
        return f"Teacher(name='{self.name}', surname='{self.surname}', subject='{self.subject}')"

class Entrant(Student):
    year_admission = None

    def __init__(self, name, surname, faculty, specialty, year_admission):
        super().__init__(name, surname, faculty, specialty)
        self.year_admission = year_admission

    def __repr__(self):
        return f"Entrant(name='{self.name}', surname='{self.surname}', faculty='{self.faculty}', specialty='{self.specialty}',  year_admission='{self.year_admission}')"

student1 = Student('Hermione', 'Granger', 'Gryffindor', 172)
print(student1)  

teacher1 = Teacher('Severus', 'Snape', 'Potions Master')
print(teacher1)  

entrant1 = Entrant( 'Draco ', 'Malfoy', 'Slytherin', '172', 2023)
print(entrant1)  