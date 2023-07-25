from flask import Blueprint, jsonify, request
from models.people import People

api = Blueprint('api_peoples', __name__)

# [GET] /people Get a list of all the people in the database
# [GET] /people/<int:people_id>

@api.route('/people' , methods=['GET'])
def list_people():
    
    people = People.query.all() # [<People 1>, <People 2>]
    people = list(map(lambda character: character.serialize(), people)) # [{"id": 1}, {"id": 2}]
    
    return jsonify('People:',people), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def list_specific_people(people_id):

    character = People.query.filter_by(id=people_id).first()

    return jsonify('Character:',character.serialize()), 200