from extensions import db

class Supplier(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(250), nullable=True)
    availability = db.Column(db.Boolean, nullable=True)
    country = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(250), nullable=True)    
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'availability':self.availability,
            'country':self.country,
            'email': self.email
        }