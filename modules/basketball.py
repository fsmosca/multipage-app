import streamlit as st
import pandas as pd


@st.cache_data(ttl='7d')
def ranking():
    fn = 'data/basketball/2024/fiba/men/team_ranking_2024-02-27.csv'
    return pd.read_csv(fn, delimiter=';')


def TeamRanking():
    with st.container(border=True):
        st.markdown(
            '''
            ### FIBA World Ranking
            **5x5 Basketball Men's Team**  
            :red[2024-02-27]
            '''
        )
        st.dataframe(
            ranking(),
            height=300,
            use_container_width=True,
            hide_index=True
        )
        st.markdown(
            '''
            source: [FIBA basketball](https://www.fiba.basketball/rankingmen)
            '''
        )
