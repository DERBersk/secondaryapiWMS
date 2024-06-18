from flask import Blueprint, jsonify

from models.material import Material

m_bp = Blueprint('material', __name__, url_prefix='/material')

###################################################
# Get for multiple materials
###################################################
@m_bp.route('/', methods=['GET'])
def get_materials():
    materials = Material.query.all()
    return jsonify([m.serialize() for m in materials])
