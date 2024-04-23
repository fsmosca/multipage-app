import streamlit as st
from modules.nav import Nav
from modules.home import BALL_SPORTS


st.set_page_config(
    layout='centered',
    page_title='Sports'
)


def main():
    Nav()
    st.header('🏡 Home')

    st.markdown(BALL_SPORTS)


if __name__ == '__main__':
    main()
