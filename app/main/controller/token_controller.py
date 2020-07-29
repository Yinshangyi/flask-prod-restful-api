from app.main.utils.dto import TokenDto
from flask_restplus import Resource
from flask import request, Response, jsonify
from app.main.services.auth import is_user_auth, generate_jwt, token_required

api = TokenDto.api
user_login_info = TokenDto.user_login_info


@api.route('/')
class JwtToken(Resource):
    @api.doc('Get a new JWT token')
    @api.expect(user_login_info, validate=False)
    def post(self):
        username = request.json['username']
        password = request.json['password']

        if not is_user_auth(username, password):
            return Response(status=401)

        token = generate_jwt(username, 0)
        return jsonify({'token': token.decode('UTF-8')})
