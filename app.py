import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.set_page_config(
   page_title="Movie Recommender System",
   page_icon="🎬",
   layout="centered",
   initial_sidebar_state="expanded",
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=79ebe84d90ce158a3ca21b17e5c3ad2a&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(selected):
    movie_index = movies[movies['title'] == selected].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True,key = lambda x: x[1])[1:11]
    recommended_movies = []
    movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        movie_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, movie_poster


st.title('Movie Recommender System')
selected_movie = st.selectbox('Select Movie',movies['title'].values)
if st.button('Recommend'):
    names,posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3], )
    
    with col5:
        st.text(names[4])
        st.image(posters[4])
    
    with col6:
        st.text(names[5])
        st.image(posters[5])

    with col7:
        st.text(names[6])
        st.image(posters[6])

    with col8:
        st.text(names[7])
        st.image(posters[7])
    
    with col9:
        st.text(names[8])
        st.image(posters[8])
    
    with col10:
        st.text(names[9])
        st.image(posters[9])