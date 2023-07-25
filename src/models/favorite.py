from models import db

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey('peoples.id'), default=1)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()