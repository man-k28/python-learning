from application import db


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    lessons = db.relationship('Lesson', backref='teacher')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Teacher {self.name}>"