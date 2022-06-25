import streamlit as st

import pickle
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    index_value = new_df[new_df["Tittle"]==movie].index[0]
    distances = similarity[index_value]
    movie_list=  sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    _5_recommend_movie=[]
    _5_recommend_movie_posters = []

    for i in movie_list:
        movie_id = new_df.iloc[i[0]].movie_id

        _5_recommend_movie_posters.append(fetch_poster(movie_id))
        _5_recommend_movie.append(new_df.iloc[i[0]].Tittle)

    return _5_recommend_movie,_5_recommend_movie_posters

new_df1 = pickle.load(open('new_df.pkl','rb'))
new_df = pickle.load(open('movies.pkl','rb'))
#similarity= pickle.load(open('similarity.pkl','rb'))
All_movies= new_df["Tittle"].values
cv = pickle.load(open('cv.pkl','rb'))
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
vectors = cv.fit_transform(new_df1['Tags']).toarray()
similarity = cosine_similarity(vectors)

st.title('MOVIE  RECOMMENDATION  SYSTEM')


movie_name = st.selectbox("Select a Movie",All_movies)
if st.button("Recommend"):
    names,posters = recommend(movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
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
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
