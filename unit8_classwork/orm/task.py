from application import db


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    task_content = db.Column(db.String())
    qualify = db.Column(db.Integer())
    task_category_id = db.Column(db.ForeignKey('category.id'))
    student_tasks = db.relationship('StudentTask', backref='task')
    lesson_tasks = db.relationship('LessonTask', backref='task')

    def __init__(self, task_content, qualify, task_category):
        self.task_content = task_content
        self.qualify = qualify
        self.task_category_id = task_category

    def __repr__(self):
        return f"<Task {self.task_content} {self.qualify}>"