from flask_restplus import Namespace, fields


class PostDto:
    api = Namespace('post', description='post related operations')
    post = api.model('post', {
        'title': fields.String(required=True, description='Title of the post'),
        'content': fields.String(required=True, description='Content of the post'),
    })


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'posts': fields.Nested(PostDto.post),
    })