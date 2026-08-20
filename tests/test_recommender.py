from data_prep import load_movie_lens


def test_movie_lens_data_loads():
    movies, ratings = load_movie_lens()

    assert movies is not None
    assert ratings is not None
    assert len(movies) > 0
    assert len(ratings) > 0