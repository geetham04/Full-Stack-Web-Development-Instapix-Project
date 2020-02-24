from flask import redirect, request, url_for, render_template, session, flash
# from flask.ext.session import Session
from flask.views import MethodView
import dbmodel

class login(MethodView):
    def get(self):
        return render_template('login.html')
    
    def post(self):
        model = dbmodel.get_model()

        user_input = {}
        user_input["username"] = request.form['username']
        user_input["password"] = request.form['password']

        status = model.login(user_input)
        if status is True:
            session['user_id'] = user_input["username"]
            profile_photo = model.get_profile_photo(session['user_id'])
            session['profile_photo'] = profile_photo[0]
            return redirect(url_for('newsfeed', profile_photo=profile_photo))
        else:
            flash('sign in failed, incorrect username or password', 'danger')        
            return render_template('login.html')

        