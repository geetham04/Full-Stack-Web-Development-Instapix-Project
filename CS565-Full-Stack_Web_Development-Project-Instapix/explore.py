from flask import redirect, request, url_for, render_template, session
from flask.views import MethodView
import dbmodel

class explore(MethodView):
    def get(self):
        model = dbmodel.get_model()
        current_user = session['user_id']
        current_user_photo = session['profile_photo']
        users = model.get_suggested_followees(current_user)
        return render_template("explore.html", users=users, current_user_photo=current_user_photo, current_user=current_user)

    def post(self):
        model = dbmodel.get_model()
        follower = session['user_id']
        followee_list = request.form.getlist('follow-check-box')
        for followee in followee_list:
            model.add_to_user_follow(follower, followee)
        return redirect(url_for('newsfeed'))
