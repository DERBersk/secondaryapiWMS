from flask import Blueprint, jsonify

from models.order import Order

o_bp = Blueprint('order', __name__, url_prefix='/order')

###################################################
# Get for multiple orders
###################################################
@o_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([o.serialize() for o in orders])
