from app.main import db


def get_all(model):
    return model.query.all()


def get_a_user(model, public_id):
    return model.query.filter_by(id=1).first()


def save_new_item(data):
    db.session.add(data)
    db.session.commit()