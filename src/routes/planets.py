from flask import Blueprint, jsonify, request
from models.planet import Planet

api = Blueprint('api_planets', __name__)

# [GET] /planets Get a list of all the planets in the database
# [GET] /planets/<int:planet_id> Get one single planet information

@api.route('/planets' , methods=['GET'])
def list_planets():
    
    planets = Planet.query.all() # [<People 1>, <People 2>]
    planets = list(map(lambda planet: planet.serialize(), planets)) # [{"id": 1}, {"id": 2}]
    
    return jsonify('Planetas:',planets), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def list_specific_planet(planet_id):

    planet = Planet.query.filter_by(id=planet_id).first()

    return jsonify('Planet:',planet.serialize()), 200