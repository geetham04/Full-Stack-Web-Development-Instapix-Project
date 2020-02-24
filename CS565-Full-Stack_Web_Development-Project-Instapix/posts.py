from flask import redirect, request, url_for, render_template, session
from flask.views import MethodView
import dbmodel
import os
import base64
from werkzeug.utils import secure_filename

# POST_UPLOAD_FOLDER = "/home/sanjukta/Desktop/Geetha/CS565-Full-Stack_Web_Development-Project-Instagram/uploads"
POST_UPLOAD_FOLDER = "/Users/sanjuktadas/Desktop/OneDrive/_PSU/courses/2019/FALL_2019/CS565-Full_Stack_Web_Development/GIT/Final_Project/instapix/CS565-Full-Stack_Web_Development-Project-Instagram/uploads"


class posts(MethodView):
    def get(self):
        current_user = session['user_id']
        profile_photo = session['profile_photo']

        return render_template('posts.html',  profile_photo=profile_photo, current_user=current_user)
    
    def post(self):
        model = dbmodel.get_model()
        # print(request.form['pictures'])
        file = request.files['picture']
        description = request.form['description'] 
        self.store_photo(model, file, description)
        return redirect(url_for('newsfeed'))
    
    def store_photo(self, model, file, description):
        filename = secure_filename(file.filename)
        file_key  =str(base64.b64encode(str(filename).encode("utf-8")))
        model.store_media_id(file_key)
        file_path = os.path.join(POST_UPLOAD_FOLDER, file_key)
        file.save(file_path)
        user_id = session['user_id']
        model.store_media_metadata(file_key, user_id, description)

