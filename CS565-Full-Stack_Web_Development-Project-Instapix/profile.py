from flask import redirect, request, url_for, render_template, session
from flask.views import MethodView
import dbmodel

class profile(MethodView):
    def get(self):
        model = dbmodel.get_model()
        current_user = session['user_id']
        metadata_list = model.get_media_metadata(current_user)
        current_user_photo = session['profile_photo']
        
        return render_template("profile.html", metadata_list=metadata_list, current_user_photo=current_user_photo, current_user=current_user)

    # def post(self):
    #     model = dbmodel.get_model()
	#     return render_template("profile.html", users=users)
