from flask import redirect, request, url_for, render_template, flash
from flask.views import MethodView
import dbmodel
import os
import base64
from werkzeug.utils import secure_filename

# PROFILE_PHOTO_UPLOAD_FOLDER = "/home/sanjukta/Desktop/Geetha/CS565-Full-Stack_Web_Development-Project-Instagram/uploads"
PROFILE_PHOTO_UPLOAD_FOLDER = "/Users/sanjuktadas/Desktop/OneDrive/_PSU/courses/2019/FALL_2019/CS565-Full_Stack_Web_Development/GIT/Final_Project/instapix/CS565-Full-Stack_Web_Development-Project-Instagram/uploads"

class index(MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        model = dbmodel.get_model()

        user_input = {}
        user_input["email"] = request.form['email']
        user_input["name"] = request.form['name']
        user_input["username"] = request.form['username']
        user_input["password"] = request.form['password']
        file = request.files['picture']
        self.store_photo(model, file, user_input)
        flash('sign up successful, please login to continue', 'info')        
        return render_template('index.html')

    def store_photo(self, model, file, user_input):
        filename = secure_filename(file.filename)
        file_key  =str(base64.b64encode(str(filename).encode("utf-8")))
        model.store_media_id(file_key)
        file_path = os.path.join(PROFILE_PHOTO_UPLOAD_FOLDER, file_key)
        file.save(file_path)
        # model.store_media_metadata(file_key, user_id, description)
        model.sign_up(user_input, file_key)