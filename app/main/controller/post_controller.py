from flask import request, Response
from flask_restplus import Resource

from app.main.utils.dto import PostDto
from app.main.models.post import Post
from flask_restplus import fields
from app.main.services.controller_service import get_all, save_new_item
from app.main.services.auth import token_required

api = PostDto.api
_post = PostDto.post

resource_fields = {
    'title': fields.String,
    'content': fields.String,
}


@api.route('/')
class PostList(Resource):
    @api.doc('List of registered posts')
    @token_required
    @api.marshal_list_with(_post, envelope='data')
    def get(self):
        return get_all(Post)

    @api.doc('Create a new post')
    @token_required
    @api.expect(_post, validate=True)
    def post(self):
        data = request.json
        new_post = Post(title=data['title'], content=data['content'])
        save_new_item(new_post)
        return Response(status=201)