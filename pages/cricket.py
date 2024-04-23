import streamlit as st
from modules.nav import Nav
from modules.cricket import TeamRanking


st.set_page_config(
    layout='centered',
    page_title='Cricket',
    page_icon='🏆'
)


def main():
    Nav()
    st.header('🏏 Cricket')
    st.divider()

    TeamRanking()


if __name__ == '__main__':
    main()
