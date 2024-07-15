from flask import Blueprint, jsonify

from models.order import Order

o_bp = Blueprint('order', __name__, url_prefix='/order')

###################################################
# Get for multiple Orders
###################################################
@o_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([o.serialize() for o in orders])

###################################################
# Get for a single Orders
###################################################
@o_bp.route('/<string:supplier_id>', methods=['GET'])
def get_orders_from_supplier(supplier_id):
    orders = Order.query.filter(Order.supplier_id == supplier_id).all()
    return jsonify([o.serialize() for o in orders])