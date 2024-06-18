from flask import Blueprint, jsonify
from models.supplier import Supplier

s_bp = Blueprint('supplier', __name__, url_prefix='/supplier')

###################################################
# Get for multiple suppliers
###################################################
@s_bp.route('/', methods=['GET'])
def get_supplier():
    supplier = Supplier.query.all()
    return jsonify([s.serialize() for s in supplier])
