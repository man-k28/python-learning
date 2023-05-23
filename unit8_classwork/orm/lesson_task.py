from application import db


class LessonTask(db.Model):
    __tablename__ = 'lesson_task'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.ForeignKey('task.id'))
    lesson_id = db.Column(db.ForeignKey('lesson.id'))

    def __init__(self, task, lesson):
        self.task_id = task
        self.lesson_id = lesson

    def __repr__(self):
        return f"<LessonTask {self.id}>"