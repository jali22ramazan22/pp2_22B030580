def imdb_above_55(movie):

    return movie["imdb"] > 5.5


def imdb_above_55_list(movies):

    return [movie for movie in movies if imdb_above_55(movie)]


def filter_by_category(movies, category):

    return [movie for movie in movies if movie["category"] == category]


def avg_imdb_score(movies):

    if not movies:
        return 0
    total = sum(movie["imdb"] for movie in movies)
    return total / len(movies)


def avg_imdb_score_by_category(movies, category):

    category_movies = filter_by_category(movies, category)
    return avg_imdb_score(category_movies)
