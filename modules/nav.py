import streamlit as st


def Home():
    st.sidebar.page_link('streamlit_app.py', label='Home', icon='🏡')


def Baseball():
    st.sidebar.page_link('pages/baseball.py', label='Baseball', icon='⚾')


def Basketball():
    st.sidebar.page_link('pages/basketball.py', label='Basketball', icon='🏀')


def Cricket():
    st.sidebar.page_link('pages/cricket.py', label='Cricket', icon='🏏')


def Chat():
    st.sidebar.page_link('pages/chat.py', label='Chat', icon='💬')


def Nav():
    Home()
    Basketball()
    Cricket()
    Baseball()
    Chat()
