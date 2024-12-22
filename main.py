class Student: # класс студенты
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Задание 2
    def estimation_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self, grades_student=0):
        count = 0
        if len(list(self.grades.values())) > 0:
            for grades in list(self.grades.values()):
                for grade in grades:
                    count += 1
                    grades_student += grade
        else:
            return 'Оценок нет'
        return grades_student / count
    # Задание 3
    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.average_score()} \n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    # Задание 3
    def __lt__(self, other):
        if self.average_score() < other.average_score():
            return f'У студента {self.surname} {self.name} среднее значение оценок по сравнению со студентом {other.surname} {other.name} хуже'
        else:
            return f'У студента {self.surname} {self.name} среднее значение оценок по сравнению со студентом {other.surname} {other.name} лучше'




class Mentor: # класс преподаватели
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}



# Задание 1
class  Lecturer(Mentor): # класс лекторы
    def average_score(self, grades_lecturer=0):
        count = 0
        if len(list(self.grades_lecturer.values())) > 0:
            for grades in list(self.grades_lecturer.values()):
                for grade in grades:
                    count += 1
                    grades_lecturer += grade
        else:
            return 'Оценок нет'
        return grades_lecturer / count

    # Задание 3
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_score()}'

    # Задание 3
    def __lt__(self, other):
        if self.average_score() < other.average_score():
            return f'У лектора {self.surname} {self.name} среднее значение оценок по сравнению с лектором {other.surname} {other.name} хуже'
        else:
            return f'У лектора {self.surname} {self.name} среднее значение оценок по сравнению с лектором {other.surname} {other.name} лучше'

# Задание 1
class Reviewer(Mentor): # класс эксперты, проверяющие домашние задания
    # Задание 2
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'




best_student = Student('Кирилл', 'Иванов', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_lector = Lecturer('Some','Buddy')
some_lector.courses_attached += ['Python']

best_lector = Lecturer('Петр','Петров')
best_lector.courses_attached += ['Python']

some_reviewer = Reviewer('Some','Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 5)
some_reviewer.rate_hw(some_student, 'Python', 6)
some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(some_student,'Git', 10)

some_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Python', 5)
some_reviewer.rate_hw(best_student,'Git', 10)

some_student.estimation_lecturer(some_lector,'Python', 10)
some_student.estimation_lecturer(some_lector,'Python', 10)

best_student.estimation_lecturer(best_lector,'Python', 10)
best_student.estimation_lecturer(best_lector,'Python', 10)

print(some_reviewer) # задание 3
print(some_lector) # задание 3
print(some_student) # задание 3
print(best_student < some_student) # задание 3
print(best_lector < some_lector) # задание 3







#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)