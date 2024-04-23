import streamlit as st
import pandas as pd


@st.cache_data(ttl='7d')
def ranking():
    fn = './data/cricket/2024/wc/t20i/team/men/rankng_2024-04-17.csv'
    return pd.read_csv(fn)


def TeamRanking():
    with st.container(border=True):
        st.markdown(
            '''
            ### World Cup
            **T20 International Team Ranking**  
            :red[2024-04-17]
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
            source: [WC cricket](https://www.icc-cricket.com/rankings/team-rankings/mens/t20i)
            '''
        )
