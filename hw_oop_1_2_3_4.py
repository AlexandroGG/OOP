class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_hwlist(self):
        rate_courses_lst = self.grades.values()
        grades = []
        for grade in rate_courses_lst:
            grades += grade
        if len(grades) == 0:
            self.avg_student = 0
        else:
            self.avg_student = sum(grades) / len(grades)
        return self.avg_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
        else:
            return self.avg_student < other.avg_student   

    def __str__(self):
        some_student = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.rate_hwlist()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return some_student

class Mentor:    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self):
        some_reviewer = f"Имя: {self.name}\nФамилия: {self.surname}"
        return some_reviewer
                   
class Lecturer(Mentor):    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_grades = {}

    def average_courses_grades(self):
    
        rate_courses_lst = self.courses_grades.values()
        grades = []
        for grade in rate_courses_lst:
            grades += grade
        if len(grades) == 0:
            self.avg_lecturer = 0
        else:
            self.avg_lecturer = sum(grades) / len(grades)
        return self.avg_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
        else:
            return self.avg_lecturer < other.avg_lecturer             
    
    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_courses_grades()}'
        return some_lecturer

student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2 = Student('Василий', 'Петров', 'male')
student_2.courses_in_progress += ['Kotlin']
student_2.finished_courses += ['Java']

reviewer_1 = Reviewer('Марк', 'Захарыч')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Евгений', 'Петрович')
reviewer_2.courses_attached += ['Kotlin', 'Java']

lecturer_1 = Lecturer('Аркадий', 'Иванович')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Елизавета', 'Семеновна')
lecturer_2.courses_attached += ['Kotlin', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Kotlin', 7)
reviewer_2.rate_hw(student_2, 'Kotlin', 9)
reviewer_2.rate_hw(student_2, 'Java', 8)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Kotlin', 9)
student_2.rate_lecture(lecturer_2, 'Kotlin', 7)
print('Оценки студентов:')
print('Оценки студента 1', student_1.grades)
print('Оценки студента 2', student_2.grades)

print()
print('Оценки лекторов:')
print('Оценки лектора 1', lecturer_1.courses_grades)
print('Оценки лектора 2', lecturer_2.courses_grades)

print()
print('Список проверяющих:')
print(reviewer_1)
print(reviewer_2)
print()
print('Список лекторов:')
print(lecturer_1)
print(lecturer_2)
print()
print('Список студентов:')
print(student_1)
print(student_2)
print()
print('Сравнение студентов по средней оценке за ДЗ:')
print(student_1 < student_2)
print(student_1 > student_2)
print(student_1.__lt__(student_2))
print()
print('Сравнение лекторов по средней оценке за лекции:')
print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1.__lt__(lecturer_2))

students_lst = [student_1, student_2]
def students_avg_grades(student_lst, course):
    students_grades_lst = []
    for student in student_lst:
        if course in student.grades.keys():
            students_grades_lst.extend(student.grades.values())
    for grades in students_grades_lst:
        student_avg_grade = sum(grades) / len(grades)
    print(f'Cредняя оценка за домашние задания по всем студентам в рамках конкретного курса {course}: {student_avg_grade}')

lecturers_lst = [lecturer_1, lecturer_2]
def lecturers_avg_grades(lecturers_lst, course):
    lecturer_grades_lst = []
    for lecturer in lecturers_lst:
        if course in lecturer.courses_grades.keys():
                lecturer_grades_lst.extend(lecturer.courses_grades.values())
    for grades in lecturer_grades_lst:
        avg_lecturer_grade = sum(grades) / len(grades)    
    print(f'Средняя оценка за лекции всех лекторов в рамках курса {course}: {avg_lecturer_grade}')
    
print()
students_avg_grades(students_lst, 'Python')
lecturers_avg_grades(lecturers_lst, 'Kotlin')
        
