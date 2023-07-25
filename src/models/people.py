from models import db
from datetime import datetime

class People(db.Model):
    __tablename__ = 'peoples'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(20))
    mass = db.Column(db.String(20))
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.DateTime, default=datetime.now)
    gender = db.Column(db.String(10))
    name = db.Column(db.String(100))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "name": self.name,
            "planet_id": self.planet_id
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()