import streamlit as st
import pickle
import pandas as pd
import numpy as np

song_dict = pickle.load(open('song.pkl', 'rb'))
song = pd.DataFrame(song_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

avg = np.mean(song['Rating'])

def recommend(obj):
    song_index = song[song['Song'] == obj].index[0]
    distance = similarity[song_index]
    L = []
    song_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:]
    index = []
    for i in song_list:
        index.append(i[0])
    count = 0
    for i in index:
        x = song['Rating'][i]
        if (x > avg):
            if(count < 5):
                count += 1
                L.append(song['Song'][i])          
            else:
                break
    return L

st.title('Song Recommender System')

selected_song_name = st.selectbox(
    'Check Out',
    song['Song'].values
)

x = recommend(selected_song_name)
for i in x:
    st.text(i)