from app.main import db


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))