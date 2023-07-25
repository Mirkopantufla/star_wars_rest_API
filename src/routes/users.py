from flask import Blueprint, jsonify, request
from models.user import User

api = Blueprint('api_users', __name__)

# [GET] /users Get a list of all the blog post users
# [GET] /users/favorites Get all the favorites that belong to the current user.

@api.route('/users' , methods=['GET'])
def list_users():
    
    users = User.query.all() # [<People 1>, <People 2>]
    users = list(map(lambda user: user.serialize(), users)) # [{"id": 1}, {"id": 2}]
    
    return jsonify('Users:',users), 200

@api.route('/users/<int:id_propio>/favorites', methods=['GET'])
def list_user_with_favorites(id_propio):

    planet = User.query.filter_by(id=id_propio).first()

    return jsonify('Planet:',planet.serialize_with_favorites()), 200