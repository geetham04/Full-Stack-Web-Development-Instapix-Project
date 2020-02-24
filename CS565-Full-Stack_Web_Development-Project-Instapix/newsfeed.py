from flask import redirect, request, url_for, render_template, session
from flask.views import MethodView
import dbmodel

class newsfeed(MethodView):
    def get(self):
        model = dbmodel.get_model()
        current_user = session['user_id']
        current_user_photo = session['profile_photo']
        feed = {}
        followee_profile_photo = {}
        followees = model.get_all_followees(current_user)
        for followee in followees:
            metadata_list = model.get_media_metadata(followee[1])
            if metadata_list is not None:
                feed[followee[1]] = metadata_list
                profile_photo = model.get_profile_photo(followee[1])
                followee_profile_photo[followee[1]] = profile_photo[0]
        return render_template('newsfeed.html', feed=feed, followee_profile_photo=followee_profile_photo, current_user_photo=current_user_photo, current_user=current_user)