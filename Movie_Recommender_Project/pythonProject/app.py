import streamlit as st
import Register
import all_movies
import login
import recommendations
import Home

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False


    page = st.sidebar.selectbox("Select Page",
                                ["Home", "All Movies", "Movie Recommendations", "Login", "Register", "Logout"])

    if page =="Home":
        Home.main()
    elif page == "All Movies":
        if st.session_state.logged_in:
            all_movies.main()
        else:
            st.warning("Please login to access this page. If you are a new user, please register [here](register()).")
    elif page == "Movie Recommendations":
        if st.session_state.logged_in:
            recommendations.main()
        else:
            st.warning("Please login to access this page. If you are a new user, please register [here](register()).")
    elif page == "Login":
        if not st.session_state.logged_in:
            st.session_state.logged_in = login.main()
            if st.session_state.logged_in:
                st.title("Login Successful")
                st.write("You have successfully logged in!")
        else:
            st.title("Already Logged In")
            st.write("You are already logged in.")

    elif page == "Register":
        if not st.session_state.logged_in:
            registration_success = Register.main()
            if registration_success:
                st.title("Registration Successful")
                st.write("You have successfully registered!")
        else:
            st.warning("Please logout before registering a new account.")
    elif page == "Logout":
        if st.session_state.logged_in:
            st.session_state.logged_in = False
            st.title("Logout Successful")
            st.write("You have successfully logged out!")
        else:
            st.warning("You are not logged in.")


if __name__ == "__main__":
    main()
