

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    'movies':'sqlite:///movies.db',
    'users':'sqlite:///users.db',
    'movies_to_users':'sqlite:///movie_to_user.db'
}

class Movie(db.Model):
    __bind__key__ = 'movies'
    # This class will be used to create the table in the database for the movies
    pass
class Movie_to_user(db.Model):
    __bind__key__ = 'movies_to_users'
    # This class will be used to create the table in the database, it represents relationship between the movie and the user
    pass
class User(db.Model):
    __bind__key__ = 'users'
    # This class will be used to create the table in the database for the users
    pass

@app.route('/')
def index():
    return render_template('index.html')

# This search function below will extract the movies from the database and display them on the search page
@app.route('/search', methods=['GET'])
def search(movie_name):
    return render_template('search.html')

# This recommend function below will recommend the movies to the user based on the movie name entered by the user
@app.route('/recommend/<movie_name>')
def recommend(movie_name):
    return render_template('recommend.html')

if __name__ =="__main__":
    app.run(debug=True)