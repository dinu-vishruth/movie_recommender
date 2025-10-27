# Movie Recommendation System — Full Project

This repository contains a Streamlit app and core code for a MovieLens-based recommender system.
It uses the MovieLens 100k dataset (not included). Download the dataset from:
https://grouplens.org/datasets/movielens/100k/

## Structure
- app/: Streamlit application and core modules
- data/: put `u.data` and `u.item` (from MovieLens 100k) here
- notebooks/: exploratory notebook (not included—use the app code as guide)

## Quick start
1. Download MovieLens 100k and place `u.data` and `u.item` into `data/`.
2. Create a virtualenv and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```
