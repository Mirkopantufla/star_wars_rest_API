from models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    favorites = db.relationship("Favorite", backref="user", lazy="dynamic")
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
    
    def serialize_with_favorites(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "favorites": self.get_favorites()
        }
    
    def get_favorites(self):
        return list(map(lambda favorite: favorite.serialize(), self.favorites)) #[{"id": 1}, {"id": 2}]
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()