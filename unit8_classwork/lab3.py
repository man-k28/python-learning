#todo:

#  Установить FLASK, установить SQLAlchemy
#  Настроить ORM на базу PostgresSQL
#  Для модели  БД "Система проверки задач" создать ORM модель. Сгенерировать ее в БД.
#  Переписать запросы с SQL на ORM


# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
# https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
# https://habr.com/ru/companies/yandex/articles/511892/

# Создать интерфейсы ввода GUI согласно бизнес логики.

from application import app, db
from orm.lesson import Lesson
from orm.teacher import Teacher
from orm.task_status import TaskStatus
from orm.category import Category
from orm.task import Task
from orm.student import Student
from orm.group import Group
from orm.group_lesson import GroupLesson
from orm.group_student import GroupStudent
from orm.lesson_task import LessonTask
from orm.student_task import StudentTask


@app.route("/")
def hello_world():
    db.create_all()
    db.session.add(Teacher(name='Учитель №1'))

    db.session.add(Student('Васечкин'))
    db.session.add(Student('Петров'))
    db.session.add(Student('Сидоров'))

    db.session.add(Category('История науки'))
    db.session.add(Category('Философия'))
    db.session.add(Category('Математика'))

    db.session.add(TaskStatus('Выполнено'))
    db.session.add(TaskStatus('Не выполнено'))

    db.session.add(Group())

    db.session.add(Lesson(1, 1))
    db.session.add(Lesson(2, 1))
    db.session.add(Lesson(3, 1))

    db.session.add(Task('Задача 1', 80, 1))
    db.session.add(Task('Задача 2', 70, 1))
    db.session.add(Task('Задача 3', 80, 2))
    db.session.add(Task('Задача 4', 80, 2))
    db.session.add(Task('Задача 5', 70, 3))
    db.session.add(Task('Задача 6', 65, 3))

    db.session.add(GroupLesson(1, 1))
    db.session.add(GroupLesson(1, 2))
    db.session.add(GroupLesson(1, 3))

    db.session.add(GroupStudent(1, 1))
    db.session.add(GroupStudent(2, 1))
    db.session.add(GroupStudent(3, 1))

    db.session.add(LessonTask(1, 1))
    db.session.add(LessonTask(2, 1))
    db.session.add(LessonTask(1, 2))
    db.session.add(LessonTask(2, 2))
    db.session.add(LessonTask(1, 3))
    db.session.add(LessonTask(2, 3))

    db.session.add(StudentTask(1, 'Результат задачи 1', 1, 1))
    db.session.add(StudentTask(2, 'Результат задачи 2', 1, 2))
    db.session.add(StudentTask(1, 'Результат задачи 3', 1, 3))
    db.session.add(StudentTask(1, 'Результат задачи 4', 1, 4))
    db.session.add(StudentTask(2, 'Результат задачи 5', 1, 5))
    db.session.add(StudentTask(1, 'Результат задачи 6', 1, 6))

    db.session.add(StudentTask(2, 'Результат задачи 1', 2, 1))
    db.session.add(StudentTask(1, 'Результат задачи 2', 2, 2))
    db.session.add(StudentTask(2, 'Результат задачи 3', 2, 3))
    db.session.add(StudentTask(1, 'Результат задачи 4', 2, 4))
    db.session.add(StudentTask(1, 'Результат задачи 5', 2, 5))
    db.session.add(StudentTask(1, 'Результат задачи 6', 2, 6))

    db.session.add(StudentTask(1, 'Результат задачи 1', 3, 1))
    db.session.add(StudentTask(1, 'Результат задачи 2', 3, 2))
    db.session.add(StudentTask(1, 'Результат задачи 3', 3, 3))
    db.session.add(StudentTask(1, 'Результат задачи 4', 3, 4))
    db.session.add(StudentTask(1, 'Результат задачи 5', 3, 5))
    db.session.add(StudentTask(2, 'Результат задачи 6', 3, 6))

    db.session.commit()
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)
