import pytesseract
from flask import Blueprint, request
from flask_restx import Api, Resource
from PIL import Image
from pytesseract import Output

ocr_blueprint = Blueprint("ocr", __name__)
api = Api(ocr_blueprint)


class Ocr(Resource):
    def post(self):
        file = request.files["file"]
        image = Image.open(file.stream)

        image = image.convert("L")

        boxes = pytesseract.image_to_data(image, output_type=Output.DICT)

        response_object = []
        n_boxes = len(boxes["text"])
        for i in range(n_boxes):
            if int(boxes["conf"][i]) > 60:
                if boxes["text"][i] and boxes["text"][i] != " ":
                    response_object.append(
                        {
                            "left": boxes["left"][i],
                            "top": boxes["top"][i],
                            "right": boxes["left"][i] + boxes["width"][i],
                            "bottom": boxes["top"][i] + boxes["height"][i],
                            "text": boxes["text"][i],
                        }
                    )
        return response_object, 200


api.add_resource(Ocr, "/ocr")
