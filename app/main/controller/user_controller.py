from flask import request, Response
from flask_restplus import Resource

from app.main.utils.dto import UserDto
from app.main.services.controller_service import get_all, save_new_item, get_a_user
from app.main.models.user import User
import datetime


api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        users = get_all(User)
        return users

    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        new_user = User(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
         )
        save_new_item(new_user)
        return Response(status=201)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class UserWithId(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(User, public_id)
        if not user:
            api.abort(404)
        else:
            return user
