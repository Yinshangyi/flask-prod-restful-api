from app.main import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    posts = db.relationship('Post', backref='user')
