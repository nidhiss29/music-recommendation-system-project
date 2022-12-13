import pickle
import streamlit as st
import pandas as pd
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('music1.jpg')

def recommend(song):
    song_index = songs[songs['title'] == song].index[0]
    distances = similarity[song_index]
    song_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_songs = []
    for i in song_list:
        recommended_songs.append(songs.iloc[i[0]].title)
    return recommended_songs

songs_dict = pickle.load(open('song_dict.pkl','rb'))
songs = pd.DataFrame(songs_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Music Recommender System')

selected_song_name = st.selectbox(
    'Select a song',songs['title'].values
)



if st.button('Recommend'):
    recommendations = recommend(selected_song_name)
    for i in recommendations:
        st.write(i)