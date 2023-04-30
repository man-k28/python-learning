#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.

import random
import copy

class Task:
    __finished = False
    __selected_answer = None
    __correct_answer = 1
    __variants_cnt = 3
    __qualify = 50
    __name = 'Задача '

    def __init__(self, index):
        self.__name = self.__name + str(index)
        self.__variants_cnt = random.randint(self.__variants_cnt, 6)
        self.__correct_answer = random.randint(1, self.__variants_cnt)
        self.__qualify = random.randint(40, 80)

    @property
    def variants_cnt(self):
        return self.__variants_cnt
    
    @property
    def qualify(self):
        return self.__qualify
    
    @property
    def name(self):
        return self.__name

    @property
    def finished(self) -> bool:
        return self.__finished

    def finish(self, selected_answer):
        self.__selected_answer = selected_answer
        self.__finished = True

    def isCorrect(self) -> bool:
        return self.__finished and self.__correct_answer == self.__selected_answer



class Pupil:
    __qualify = 80 # Уровень знаний ученика
    __name = ''

    def __init__(self, name):
        self.__qualify = random.randint(40, 95) #гениев не держим
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def processTask(self, task:Task) -> Task:
        if (self.__qualify >= task.qualify):
            answer = random.randint(1, task.variants_cnt + 1)
            task.finish(answer)
        return task

class Lesson:
    __task_cnt = 0
    __tasks = []
    __working_progress = {}
    __pupils = []

    def __init__(self):
        self.__task_cnt = random.randint(10, 15);
        self.__tasks = [Task(i) for i in range(1, self.__task_cnt)]

    def start(self):
        for pupil in self.__pupils:
            self.__working_progress[pupil.name] = [pupil.processTask(copy.deepcopy(task)) for task in self.__tasks.copy()]
    
    @property
    def tasks(self):
        return self.__tasks

    @property
    def results(self):
        return self.__working_progress

    def addPupil(self, pupil:Pupil):
        self.__pupils.append(pupil)


class LessonResult:
    __summary = {}
    __lesson = None
    def __init__(self, lesson:Lesson):
        self.__lesson = lesson

    def processResult(self):
        for name, tasks in self.__lesson.results.items():
            self.__summary[name] = ['+' if res.isCorrect() else '-' for res in tasks]
        return self.__summary
    
    def __str__(self):
        output = 'Имя\t| '
        for i in self.__lesson.tasks:
            output = output + i.name + ' | '
        output = output + '\n'
        for name, tasks in self.__summary.items():
            output = output + name + '\t| '
            for task in tasks:
                output = output + task + ' | '
            output = output + '\n'
        return output



class Teacher:
    global lesson
    def init_lesson(self, lesson:Lesson):
        lesson.start()

    def get_lesson_result(self, lesson:Lesson):
        result = LessonResult(lesson)
        result.processResult()
        print(result)


if __name__ == '__main__':
    pupils_name = ('Вася', 'Сеня', 'Иван', 'Дмитрий', 'Фёдор', 'Пётр', 'Сатана', 'Миша', 'Гриша', 'Потоп')
    teacher = Teacher()
    for i in range(0, 10):
        lesson = Lesson()
        for name in pupils_name:
            lesson.addPupil(Pupil(name))
        teacher.init_lesson(lesson)
        teacher.get_lesson_result(lesson)
        print('-------------')
    
