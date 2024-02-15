from flask import Flask
from app.middleware.jwt import jwt
app = Flask(__name__)

# Configure the app
app.config.from_pyfile('config/config.py')

# Import and register blueprints/routes
from app.routes.index import auth_routes_blueprint
app.register_blueprint(auth_routes_blueprint)

# Set the secret key for JWT encoding
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
# Register middleware
jwt.init_app(app)

# Import and initialize extensions (if any)
from database.db import db
db.init_app(app)