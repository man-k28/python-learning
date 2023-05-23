from application import db


class StudentTask(db.Model):
    __tablename__ = 'student_task'

    id = db.Column(db.Integer, primary_key=True)
    task_status_id = db.Column(db.ForeignKey('task_status.id'))
    task_result = db.Column(db.String())
    student_id = db.Column(db.ForeignKey('student.id'))
    task_id = db.Column(db.ForeignKey('task.id'))

    def __init__(self, task_status, task_result, student, task):
        self.task_status_id = task_status
        self.task_result = task_result
        self.student_id = student
        self.task_id = task

    def __repr__(self):
        return f"<StudentTask {self.id}>"