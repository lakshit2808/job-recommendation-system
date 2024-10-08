'''
NA Landing Page
================
NA sponership
================
Payment Plans Formation
================
Server deployment
================
'''

import streamlit as st

from Auth.Register import register
from Auth.Login import login
from Job import App

st.set_page_config(page_title="Job Recommendation")


def main():

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        App()
        if st.sidebar.button('Logout'):
            st.session_state['logged_in'] = False
            st.experimental_rerun()
    else:
        choice = st.sidebar.selectbox('Select an option', ['Login', 'Register'])
        
        if choice == 'Login':
            login()
        elif choice == 'Register':
            register()

if __name__ == "__main__":
    main()