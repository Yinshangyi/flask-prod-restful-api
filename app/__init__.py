# app/__init__.py

from flask_restplus import Api
from flask import Blueprint
from app.main.controller.user_controller import api as user_ns
from app.main.controller.post_controller import api as post_ns
from app.main.controller.token_controller import api as token_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web services'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(post_ns, path='/post')
api.add_namespace(token_ns, path='/token')
