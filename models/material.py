from extensions import db

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    safety_stock = db.Column(db.Float)
    lot_size = db.Column(db.Float)
    stock_level = db.Column(db.Float)
    unit = db.Column(db.String(50))
    
    
    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'safety_stock': self.safety_stock,
            'lot_size': self.lot_size,
            'stock_level': self.stock_level,
            'unit': self.unit
        }