from application import db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    tasks = db.relationship('Task', backref='role')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Category {self.name}>"