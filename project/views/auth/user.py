from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser

api = Namespace('users')

@api.route('/')
class UsersView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all users.
        """
        return user_service.get_all()


@api.route('/<int:user_id>/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, user_id: int):
        """
        Get user by id.
        """
        return user_service.get_one(user_id)

    def put(self, user_id: int):
        password = request.args.get('password')
        user = user_service.get_one(user_id)
        if not user:
            return {"message": "User not found"}, 404
        user_service.update_password(user, password)
        return "", 204


