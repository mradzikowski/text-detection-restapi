from flask import Blueprint
from flask_restx import Api, Resource

text_blueprint = Blueprint("ocr", __name__)
api = Api(text_blueprint)


class Text(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'text!'
        }


api.add_resource(Text, '/ocr')