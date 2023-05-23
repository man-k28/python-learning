from application import db


class GroupLesson(db.Model):
    __tablename__ = 'group_lesson'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.ForeignKey('lesson.id'))
    group_id = db.Column(db.ForeignKey('group.id'))

    def __init__(self, lesson, group):
        self.lesson_id = lesson
        self.group_id = group

    def __repr__(self):
        return f"<GroupLesson {self.id}>"