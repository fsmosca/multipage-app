import streamlit as st
from modules.nav import Nav


st.set_page_config(
    layout='centered',
    page_title='Basketball',
    page_icon='🏆'
)


def main():
    Nav()
    st.header('🏀 Basketball')

    # Other stuff


if __name__ == '__main__':
    main()
