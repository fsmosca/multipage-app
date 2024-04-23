import streamlit as st
from modules.nav import Nav
from modules.basketball import TeamRanking


st.set_page_config(
    layout='centered',
    page_title='Basketball',
    page_icon='🏆'
)


def main():
    Nav()
    st.header('🏀 Basketball')
    st.divider()

    TeamRanking()


if __name__ == '__main__':
    main()
