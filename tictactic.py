import pandas as pd
from scipy.spatial.distance import cosi# Sample data
data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Carol'],
    'Movie': ['Inception', 'Titanic', 'Avatar', 'Inception', 'Avatar', 'Titanic', 'Avatar', 'Shrek'],
    'Rating': [5, 3, 4, 4, 5, 3, 2, 5]
}

df = pd.DataFrame(data)
df_pivot = df.pivot(index='User', columns='Movie', values='Rating').fillna(0)
print(df_pivot)
[6:51 pm, 14/6/2024] Mithilesh: # Calculate cosine similarity between users
def cosine_similarity(user1, user2):
    return 1 - cosine(user1, user2)

# User-based collaborative filtering
def get_similar_users(user, df):
    similarities = {}
    for other_user in df.index:
        if other_user != user:
            similarity = cosine_similarity(df.loc[user], df.loc[other_user])
            similarities[other_user] = similarity
    return similarities

def recommend_movies(user, df, num_recommendations=2):
    similar_users = get_similar_users(user, df)
    sorted_similar_users = sorted(similar_users.items(), key=lambda x: x[1], reverse=True)
    
    recommended_movies = {}
    for similar_user, similarity in sorted_similar_users:
        for movie in df.columns:
            if df.at[user, movie] == 0 and df.at[similar_user, movie] > 0:
                if movie not in recommended_movies:
                    recommended_movies[movie] = df.at[similar_user, movie] * similarity
                else:
                    recommended_movies[movie] += df.at[similar_user, movie] * similarity
    
    sorted_recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in sorted_recommended_movies[:num_recommendations]]

# Example recommendation for 'Alice'
print(recommend_movies('Alice', df_pivot))