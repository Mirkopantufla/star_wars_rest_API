from flask import Blueprint, jsonify, request
from models.favorite import Favorite

api = Blueprint('api_favorites', __name__)

@api.route('/favorite/planet/<int:planet_id>' , methods=['POST'])
def add_favorite_planet(planet_id):

    data = request.get_json()
    favorite = Favorite()
    favorite.planet_id = planet_id
    favorite.user_id = data['user_id']
    favorite.save()

    
    return jsonify('Planeta favorito Añadido'), 200

@api.route('/favorite/people/<int:people_id>' , methods=['POST'])
def add_favorite_character(people_id):
    
    data = request.get_json()
    favorite = Favorite()
    favorite.people_id = people_id
    favorite.user_id = data['user_id']
    favorite.save()
    
    return jsonify('Personaje favorito Añadido'), 200

# [DELETE] /favorite/planet/<int:planet_id>
# [DELETE] /favorite/people/<int:people_id>

@api.route('/favorite/planet/<int:idFrontPlanet>/delete' , methods=['DELETE'])
def delete_favorite_planet(idFrontPlanet):

    favorite = Favorite.query.filter_by(planet_id=idFrontPlanet).first()
    favorite.delete()
    
    return jsonify('Planeta Favorito Eliminado Correctamente'), 200

@api.route('/favorite/people/<int:idFrontPeople>/delete' , methods=['DELETE'])
def delete_favorite_character(idFrontPeople):

    favorite = Favorite.query.filter_by(planet_id=idFrontPeople).first()
    favorite.delete()
    
    return jsonify('Personaje Favorito Eliminado Correctamente'), 200