from application import db


class TaskStatus(db.Model):
    __tablename__ = 'task_status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<TaskStatus {self.name}>"