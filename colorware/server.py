from flask import Flask, request
from flask_restful import Api, Resource

from .firmware import firmware

app = Flask(__name__)
api = Api(app)


class UploadFirmware(Resource):
    def post(self):
        return firmware.update(
            content=request.json['content']
        )


class LogFirmware(Resource):
    def get(self):
        return dict(status=True, log=firmware.log)


api.add_resource(UploadFirmware, '/api/v1/firmware/upload')
api.add_resource(LogFirmware, '/api/v1/firmware/log')
