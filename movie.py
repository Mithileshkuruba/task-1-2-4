movies = {
    'movie1': {'genre': 'action', 'director': 'Director1', 'year': 2010},
    'movie2': {'genre': 'comedy', 'director': 'Director2', 'year': 2015},
    'movie3': {'genre': 'action', 'director': 'Director1', 'year': 2012},
    
}
user_preferences = {'genre': 'action', 'director': 'Director1'}


def recommend_movies(preferences, movies):
    recommended_movies = []
    for movie, attributes in movies.items():
        if all(attributes[attribute] == preferences[attribute] for attribute in preferences):
            recommended_movies.append(movie)
    return recommended_movies

recommendations = recommend_movies(user_preferences, movies)
print("Recommended movies:", recommendations)
