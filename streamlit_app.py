# import ptvsd
# ptvsd.enable_attach()

import streamlit as st

import pandas as pd
import numpy as np

from recommenders.utils import *

paper_titles, paper_id = load_paper_title()


def main():
    st.write('# Paper Recommender System')
    algo = st.radio("Pilih algoritma",
                    ('CCIDF (Common Citation Inverse Document Frequency)',
                     'TFIDF (Term Frequency-Inverse Document Frequency)',
                     'Hybrid (Combine CCIDF with TFIDF)'))

    st.write('### Pilih Paper yang Anda Tertarik')
    title = st.selectbox('Pilih', paper_titles)
    ids = paper_id[paper_titles.index(title)]

    if algo == 'CCIDF (Common Citation Inverse Document Frequency)':
        if st.button('Recommend'):
            try:
                with st.spinner('Mencari paper yang mirip...'):
                    top_recom = get_recommendation('CCIDF', ids, 5)

                st.title("Beberapa paper yang kami pikir mirip: ")
                for i, info in enumerate(top_recom, 1):
                    st.subheader(f'{i}. {info["title"]}')
                    st.write(f'Author: {info["author"]}')
                    st.write(f'Abstract: {info["abstract"].title()}')
            except:
                st.error("Algoritma nya masih main tenis")

    if algo == 'TFIDF (Term Frequency-Inverse Document Frequency)':
        if st.button('Recommend'):
            try:
                with st.spinner('Mencari paper yang mirip...'):
                    top_recom = get_recommendation('TFIDF', ids, 5)

                st.title("Beberapa paper yang kami pikir mirip: ")
                for i, info in enumerate(top_recom, 1):
                    st.subheader(f'{i}. {info["title"]}')
                    st.write(f'Author: {info["author"]}')
                    st.write(f'Abstract: {info["abstract"].title()}')
            except:
                st.error("Algoritma nya masih main tenis")

    if algo == 'Hybrid (Combine CCIDF with TFIDF)':
        if st.button('Recommend'):
            try:
                with st.spinner('Mencari paper yang mirip...'):
                    top_recom = get_recommendation('Hybrid', ids, 5)

                st.title("Beberapa paper yang kami pikir mirip: ")
                for i, info in enumerate(top_recom, 1):
                    st.subheader(f'{i}. {info["title"]}')
                    st.write(f'Author: {info["author"]}')
                    st.write(f'Abstract: {info["abstract"].title()}')

            except:
                st.error("Algoritma nya masih main tenis")


if __name__ == '__main__':
    main()
