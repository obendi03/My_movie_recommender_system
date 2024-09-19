import sys
import os
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)
from app import app, db, Movie  # Import app, db, and Movie class

# Get the parent directory


def read_from_csv_to_pd(filename="movies.csv", path=None):
    if path is None:
        # Set default path if not provided
        path = os.path.join(parent_dir, 'datasets', 'ml-32m')
    
    # Join the path and filename
    file_path = os.path.join(path, filename)
    
    # Ensure the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return pd.read_csv(file_path)

def init_db_from_df(df, db):
    with app.app_context():
        # Create tables for all binds
        db.create_all(bind_key=['movies'])

        for index, row in df.iterrows():
            movie = Movie(
                movieId=row['movieId'],
                title=row['title'],
                genres=row['genres']
            )
            db.session.add(movie)
        db.session.commit()

if __name__ == "__main__":
    try:
        # Load the CSV file
        df = read_from_csv_to_pd(filename="movies.csv")
        print('CSV loaded successfully.')
        
        # Initialize the database from DataFrame
        init_db_from_df(df, db)
        print("Database initialized successfully.")

    except FileNotFoundError as e:
        print(e)
    except Exception as ex:
        print(f"An error occurred: {ex}")
