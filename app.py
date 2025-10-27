import streamlit as st
from data_prep import load_movie_lens
from recommender import recommend_movies

# Load data
st.title("🎬 Movie Recommender System")

@st.cache_data
def load_data():
    movies, ratings = load_movie_lens()
    return movies, ratings

movies, ratings = load_data()

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie you like:", movie_list)

# Number of recommendations
num_recommendations = st.slider("Number of recommendations", 1, 10, 5)

# Get recommendations
if st.button("Recommend"):
    recommendations = recommend_movies(selected_movie, movies, ratings, num_recommendations)
    
    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. 🎥 {movie}")
