from flask import session
from flask_restful import Resource
from config import api

class Logout(Resource):
  def delete(self):
    print('session', session)
    if session.get('user_id'):
      session['user_id'] = None
      return {}, 200
    
    return {"error": "not logged in"}, 401

api.add_resource(Logout, '/logout')