from application import db


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    group_students = db.relationship('GroupStudent', backref='student')
    student_tasks = db.relationship('StudentTask', backref='student')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Student {self.name}>"