# app/controllers/auth_controller.py

from flask import Blueprint, request, jsonify
from app.models.user import tbl_user
from flask_jwt_extended import create_access_token

def login(request):
    data = request.get_json()
    username = data.get('username')
    phone_number = data.get('phone_number')
    user = tbl_user.query.filter_by(username=username).first()
    if user and user.phone_number == phone_number:
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401