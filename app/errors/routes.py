from app.errors import bp
from flask import jsonify


@bp.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'status':'error', 'message':'Not Found Error'}), 404


@bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({'status':'error', 'message':'Internal error'}), 500

