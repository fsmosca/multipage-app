import streamlit as st
from modules.nav import Nav


st.set_page_config(
    layout='centered',
    page_title='Sports'
)


def main():
    Nav()
    st.header('⚾ Baseball')

    # Other stuff


if __name__ == '__main__':
    main()
