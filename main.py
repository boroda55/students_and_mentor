"""
Задание № 1. Наследование
класс Mentor должен стать родительским классом,
а от него нужно реализовать наследование классов Lecturer (лекторы)
и Reviewer (эксперты, проверяющие домашние задания).
"""

"""
Задание № 2. Атрибуты и взаимодействие классов.
Теперь это могут делать только Reviewer (реализуйте такой метод)! 
А что могут делать лекторы? Получать оценки за лекции от студентов :) 
Реализуйте метод выставления оценок лекторам у класса Student 
(оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, 
в котором ключи – названия курсов, а значения – списки оценок). 
Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
"""

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




print('\nНиже представлен print на выполнение задания №3')
"""
Задание № 3. Полиморфизм и магические методы
1. Перегрузите магический метод __str__ у всех классов.
2. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
"""

print('\nДанные по проверяющему')
print(some_reviewer) # задание 3
print('\nДанные по лектору')
print(some_lector) # задание 3
print('\nДанные по студенту')
print(some_student) # задание 3
print('\nСравнение какой студент лучше обучается по оценкам')
print(best_student < some_student) # задание 3
print('\nСравнение какой лектор лучше преподает по оценкам')
print(best_lector < some_lector) # задание 3

# Задание 4
student_list = [best_student, some_student]
lectorer_list = [best_lector, some_lector]

print('\nНиже представлен print на выполнение задания №4')
"""
Задание № 4. Полевые испытания
Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).
"""
def average_student(student_list, course):
    sum_all = 0
    count_all = 0
    for student in student_list:
        if course in student.courses_in_progress:
            sum_all += student.average_score()
            count_all += 1
    return f'Средняя оценка за домашние задания по всем студентам в рамках курса  {course} равна {sum_all/count_all}'

def average_lecturer(lectorer_list , course):
    sum_all = 0
    count_all = 0
    for lecturer in lectorer_list:
        if course in lecturer.courses_attached:
            sum_all += lecturer.average_score()
            count_all += 1
    return f'Средняя оценка за лекции по всем лекторам в рамках курса  {course} равна {sum_all / count_all}'

print(average_student(student_list, 'Python'))
print(average_lecturer(lectorer_list, 'Python'))