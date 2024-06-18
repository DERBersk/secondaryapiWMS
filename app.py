# import external sources
from flask import Flask
import json
from flask_cors import CORS
# import functions and data
from extensions import db

def create_app():
    app = Flask(__name__.split(".")[0])
    CORS(app)
    
    with open('config.json', 'r') as file:
        config = json.load(file)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = config["DATABASE"]
    # Import routes
    from routes.material_routes import m_bp
    from routes.order_routes import o_bp
    from routes.supplier_routes import s_bp
    # Register blueprints
    app.register_blueprint(m_bp)
    app.register_blueprint(o_bp)
    app.register_blueprint(s_bp)
    return app

app = create_app()
db.init_app(app)
with app.app_context():
    db.create_all()
# app.run(debug=True, host='0.0.0.0')
if __name__ == "__main__":
    app.run(debug=True)