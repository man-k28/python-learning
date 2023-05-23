from application import db


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    group_students = db.relationship('GroupStudent', backref='group')
    group_lessons = db.relationship('GroupLesson', backref='group')

    def __init__(self):
        pass

    def __repr__(self):
        return f"<Group {self.id}>"