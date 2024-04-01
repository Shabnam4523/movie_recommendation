import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['Title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]

        recommended_movies.append(movies.iloc[i[0]].Title)
    return recommended_movies

movies_dict=pickle.load(open('movie_dict1.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity1.pkl','rb'))

st.title('Movie Recommender System')

selected_movie=st.selectbox(
    'welcome to my system ',
    movies['Title'].values
)
if st.button('Recommend'):
    recommendation=recommend(selected_movie)
    for Title in recommendation:
        url = movies[movies['Title'] == Title]['URLs'].values[0]
        st.write(f"[{Title}]({url})")