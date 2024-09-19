from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    'movies': 'sqlite:///movies.db',
    'users': 'sqlite:///users.db',
    'movies_to_users': 'sqlite:///movie_to_user.db',
    'tags': 'sqlite:///tags.db'
}
db = SQLAlchemy(app)

class Movie(db.Model):
    __bind_key__ = 'movies'
    movieId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genres = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Movie('{self.title}', '{self.genres}')"

class Movie_to_user(db.Model):
    __bind_key__ = 'movies_to_users'
    movieId = db.Column(db.Integer, db.ForeignKey('movies.movieId'), primary_key=True)
    imdbId = db.Column(db.Integer, nullable=False)
    tmdbId = db.Column(db.Integer, nullable=False)

class Tag(db.Model):
    __bind_key__ = 'tags'
    userId = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.Integer, db.ForeignKey('movies.movieId'), nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Tag('{self.tag}')"

class User(db.Model):
    __bind_key__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.Integer, db.ForeignKey('movies.movieId'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

# For testing purposes lisiting the movies
def list_movies(param):
    return Movie.query.limit(param).all()

# For testing purposes lisiting the movies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search(movie_name):
    return render_template('search.html')

@app.route('/recommend/<movie_name>')
def recommend(movie_name):
    return render_template('recommend.html')

if __name__ == "__main__":
    app.run(debug=True)
