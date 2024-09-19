import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from app import app,db, Movie,list_movies  # Import db and Movie class
if __name__=="__main__":
    with app.app_context():
        print(list_movies(10))
