from flask import Flask, request, jsonify, render_template
import os
import json
from flask_swagger_ui import get_swaggerui_blueprint
# from flask_sqlalchemy import SQLAlchemy

from model.json_file_model import json_files_model
from dotenv import load_dotenv

load_dotenv()

DBLINK = os.getenv('DBLINK')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DBLINK
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

SWAGGER_URL = '/docs' 
API_URL = '/static/swagger1.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "JSON uploader"
    },
)

app.register_blueprint(swaggerui_blueprint)

@app.route('/')
def home_page():
    return render_template('home.html')


from controller import json_file_controller
