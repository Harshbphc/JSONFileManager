from app import app
from model.json_file_model import json_files_model
from flask import request, jsonify, render_template
import os

obj = json_files_model()

def save_file_and_metadata(file, category):
    try:
        # Save file to the upload folder
        file_name = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)

        # Insert file metadata into the database
        obj.jsonfile_create(file_name, category)
        return {'status': 'success', 'message': 'File uploaded successfully!', 'file_name': file_name}
    except Exception as e:
        return {'status': 'error', 'message': f'Error processing the file: {e}'}

@app.route('/upload')
def upload_screen():
    categories = obj.fetch_categories()
    return render_template('upload.html', categories=categories)

@app.route('/uploaddone', methods=['POST'])
def handle_upload():
    print("Post invoked")

    file = request.files.get('file')
    category = request.form.get('category')
    result = save_file_and_metadata(file, category)
    return render_template('upload_result.html', result=result, category=category)

@app.route('/visualize')
def visualize_screen():

    categories = obj.fetch_categories()
    return render_template('visualize.html', categories = categories)

@app.route('/visualize/<category>', methods=['GET'])
def visualize_files_in_category(category):
    files = obj.fetch_files_for_category(category)  # Fetch files for the category
    return render_template('files.html', category=category, files=files, file_count=len(files))