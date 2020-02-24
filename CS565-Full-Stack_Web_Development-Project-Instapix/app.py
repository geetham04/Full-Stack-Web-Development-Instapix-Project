from flask import Flask, render_template, flash, request, url_for, redirect, session, send_from_directory
# from flask.ext.session import Session
from index import index
from login import login
from newsfeed import newsfeed
from posts import posts
from explore import explore
from profile import profile


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "super secret key"

app.add_url_rule('/',
                 view_func=index.as_view('index'),
                 methods=['GET', 'POST'])

app.add_url_rule('/login/',
                 view_func=login.as_view('login'),
                 methods=['GET', 'POST'])

app.add_url_rule('/newsfeed/',
                 view_func=newsfeed.as_view('newsfeed'),
                 methods=['GET'])

app.add_url_rule('/posts/',
                 view_func=posts.as_view('posts'),
                 methods=['GET', 'POST'])

app.add_url_rule('/explore/',
                 view_func=explore.as_view('explore'),
                 methods=['GET', 'POST'])

app.add_url_rule('/profile/',
                 view_func=profile.as_view('profile'),
                 methods=['GET', 'POST'])

@app.route('/uploads/<path:filename>')
def download_file(filename):
    # MEDIA_FOLDER = "/home/sanjukta/Desktop/Geetha/CS565-Full-Stack_Web_Development-Project-Instagram/uploads"
    MEDIA_FOLDER = "/Users/sanjuktadas/Desktop/OneDrive/_PSU/courses/2019/FALL_2019/CS565-Full_Stack_Web_Development/GIT/Final_Project/instapix/CS565-Full-Stack_Web_Development-Project-Instagram/uploads"

    return send_from_directory(MEDIA_FOLDER, filename, as_attachment=True)


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)