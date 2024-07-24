from flask_restful import Resource
from config import api


class TestConnection(Resource):
  def get(self):
    return {"message": "Successful Connection"}, 200
  

api.add_resource(TestConnection,'/')
  