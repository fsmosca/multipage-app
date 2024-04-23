import streamlit as st
from modules.nav import Nav


st.set_page_config(
    layout='centered',
    page_title='Chat on sports',
    page_icon='🏆'
)


def get_response(msg):
    return f'Hey {msg}'


def main():
    Nav()
    st.header('💬 Chat')

    if prompt := st.chat_input('enter message'):
        with st.chat_message('user'):
            st.markdown(prompt)

        response = get_response(prompt)
        with st.chat_message('assistant'):
            st.markdown(response)


if __name__ == '__main__':
    main()