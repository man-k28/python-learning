from application import db


class GroupStudent(db.Model):
    __tablename__ = 'group_student'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.ForeignKey('student.id'))
    group_id = db.Column(db.ForeignKey('group.id'))

    def __init__(self, student, group):
        self.student_id = student
        self.group_id = group

    def __repr__(self):
        return f"<GroupStudent {self.id}>"