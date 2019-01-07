from flask import Blueprint, make_response, request
from flask_restful import Resource, Api, reqparse


class RtsProvider(Resource):
    def post(self):

        postBody = str(request.data, "utf-8")
        if 'matabares' in postBody:
            file = open("L:/github_matabares/NaxcaServer/NaxcaServer/providersimulation/gimmonix/hotelSearch_3DayStay1Room1Adt.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            response = make_response(data)
            response.headers['content-type'] = 'text/xml;charset=UTF-8'
            return response
        else:
            return "<ok/>"

mod_rts = Blueprint('rts', __name__, url_prefix='/rtssimulation')
api = Api(mod_rts)

api.add_resource(RtsProvider, '/rts')