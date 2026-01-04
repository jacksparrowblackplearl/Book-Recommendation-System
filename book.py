import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np

def recommend_book(book_name):
    book_index=np.where(pt.index==book_name)[0][0]
    # book_index = pm[pm['Book-Title'] == book_name].index[0]
    distances = sb[book_index]
    book_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommend_book_names=[]
    for i in book_list[1:6]:
        # book_id = pt.iloc[[i[0]]].movie_id
        recommend_book_names.append(pt.index[i[0]])



    return recommend_book_names

st.header('Book Recommendation system')
sb = pd.read_pickle('pkl/similarity_book.pkl')
pt = pd.read_pickle('pkl/pivot_table.pkl')
book=pd.read_pickle('pkl/book.pkl')

pm = pt.reset_index()
book_list=pm['Book-Title']
selected_book = st.selectbox('select book',book_list)

if st.button('show recommendation'):

    recommend_book_names = recommend_book(selected_book)
    # print(type(recommend_book_names[0]))
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_book_names[0])
    with col2:
        st.text(recommend_book_names[1])
    with col3:
        st.text(recommend_book_names[2])
    with col4:
        st.text(recommend_book_names[3])
    with col5:
        st.text(recommend_book_names[4])

