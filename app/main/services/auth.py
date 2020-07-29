from builtins import Exception

import jwt
import datetime
from functools import wraps
from flask import request, Response, jsonify
from app.main.config import key


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response(status=403)
        token = auth_header.split(" ")[1]
        try:
            jwt.decode(token, key)
        except Exception as e:
            print(e)
            return Response(status=403)
        return func(*args, **kwargs)
    return decorated


def is_user_auth(username, password):
    """
    Check whether the user is present in the database
    :param username: username of the user
    :param password: password of the user
    :return: boolean
    """
    return True


def generate_jwt(username, delta_exp_date):
    """
    Generate a JWT token with username and the exp_date as the payload
    If delta_exp_date = 0, no expiration date will set in the payload
    :param username: username of the user
    :param delta_exp_date: delta time for the expiration date (in hours)
    :return:
    """
    payload = {
        "username": username,
    }
    if delta_exp_date != 0:
        payload["exp_date"] = datetime.datetime.utcnow() + datetime.timedelta(hours=delta_exp_date)

    new_token = jwt.encode(payload, key)
    return new_token