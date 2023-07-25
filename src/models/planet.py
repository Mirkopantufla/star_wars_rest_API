from models import db

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(100))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.Integer)
    name = db.Column(db.String(100))
    url = db.Column(db.String(200))

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "name": self.name,
            "url": self.url
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()