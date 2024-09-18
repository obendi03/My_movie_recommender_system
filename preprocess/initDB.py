
from app import app
import pandas as pd
import os
import sys
#from .. import app.db
__path__ = os.path.join("datasets", "ml-32m")

def read_from_csv_to_pd(filename="movies.csv", path = __path__):
    path = os.path.join(path, filename)
    return pd.read_csv(path)

def read_from_csv(path=__path__):
    with open(path, 'r') as f:
        return f.read()


if __name__ == "__main__":
    movies_df = read_from_csv_to_pd()
    user_df = read_from_csv_to_pd("ratings.csv")
    links_df = read_from_csv_to_pd("links.csv")
    #data = read_from_csv(path=__path__)
    #df.to_sql('movies', con=db.engine, if_exists='replace', index=False)
    print('Done')
    #print(df.head())
    print(movies_df.head())
    print("\n Here is the user data")
    print(user_df.head())
    print("\n Here is the links data")
    print(links_df.head())

    if app:
        print("app is not None")
    else:
        print("app is None")
