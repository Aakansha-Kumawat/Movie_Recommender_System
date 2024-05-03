import streamlit as st
import pickle
import requests
def main():
    st.title("All Movies")

    def fetch_movies():

        url = f"https://api.themoviedb.org/3/discover/movie?api_key=4e809196c5f1e1482555a3e76a8007c2"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            return None
    movies = fetch_movies()
    if movies:
        for movie in movies:
            st.write(f"**Title:** {movie['title']}")
            st.write(f"**Release Date:** {movie['release_date']}")
            st.write(f"**Overview:** {movie['overview']}")
            st.image(f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                     caption=movie['title'], use_column_width=True)
            st.write("---")
    else:
        st.write("Failed to fetch movie data. Please check your API key or try again later.")