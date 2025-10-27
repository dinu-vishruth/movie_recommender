import pandas as pd

def load_movie_lens():
    """
    Load MovieLens 100k dataset from the 'data' folder.
    Files needed: u.data and u.item
    """

    # Adjust the path relative to app.py
    movies_path = "../data/u.item"
    ratings_path = "../data/u.data"

    movies = pd.read_csv(
        movies_path, 
        sep='|', 
        encoding='latin-1', 
        usecols=[0, 1], 
        names=['movieId', 'title'], 
        engine='python'
    )

    ratings = pd.read_csv(
        ratings_path, 
        sep='\t', 
        names=['userId', 'movieId', 'rating', 'timestamp'], 
        engine='python'
    )

    return movies, ratings
