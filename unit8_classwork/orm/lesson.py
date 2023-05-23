from application import db


class Lesson(db.Model):
    __tablename__ = 'lesson'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer())
    group_lessons = db.relationship('GroupLesson', backref='lesson')
    lesson_tasks = db.relationship('LessonTask', backref='lesson')
    teacher_id = db.Column(db.ForeignKey("teacher.id"))

    def __init__(self, number, teacher):
        self.number = number
        self.teacher_id = teacher

    def __repr__(self):
        return f"<Lesson {self.number}>"