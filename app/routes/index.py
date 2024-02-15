# routes/auth_routes.py

from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import login

auth_routes_blueprint = Blueprint('routes', __name__)

@auth_routes_blueprint.route('/api/login', methods=['POST'])
def login_route():
    return login(request)