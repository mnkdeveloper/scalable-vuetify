# app/routes/user_route.py
from flask import jsonify, request
from flask import Blueprint
from werkzeug.utils import secure_filename

import os

from . import routes
from models.user import User
from services.user_service import UserService

@routes.route('/')
def home():
    return f"Running Flask !!"

@routes.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.path.abspath('.'), 'upload', filename))
        return 'File uploaded successfully', 200

@routes.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    elif request.method == 'POST':
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        if 'username' not in data or 'email' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        try:
            user = UserService.create_user(data['username'], data['email'])
            return jsonify(user.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
