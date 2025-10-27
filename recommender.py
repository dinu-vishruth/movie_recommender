import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def recommend_movies(selected_movie, movies, ratings, num_recommendations=5):
    """
    Recommend similar movies based on collaborative filtering.
    """

    # Merge ratings with movie titles
    merged = ratings.merge(movies, on='movieId')

    # Create a pivot table: users x movies
    user_movie_matrix = merged.pivot_table(index='userId', columns='title', values='rating')

    # Fill NaN with 0
    user_movie_matrix.fillna(0, inplace=True)

    # Compute similarity between movies
    movie_similarity = cosine_similarity(user_movie_matrix.T)

    # Convert similarity matrix to DataFrame
    movie_similarity_df = pd.DataFrame(
        movie_similarity, 
        index=user_movie_matrix.columns, 
        columns=user_movie_matrix.columns
    )

    if selected_movie not in movie_similarity_df:
        return ["Movie not found in dataset. Please try another."]

    # Sort movies by similarity
    similar_scores = movie_similarity_df[selected_movie].sort_values(ascending=False)

    # Return top N recommendations (excluding the selected movie itself)
    recommended = similar_scores.iloc[1:num_recommendations + 1].index.tolist()

    return recommended
