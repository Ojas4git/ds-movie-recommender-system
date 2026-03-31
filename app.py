import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Load data
new_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]].title)
        
    return recommended_movies

# Title
st.markdown("<h1 style='text-align: center;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<p style='text-align: center;'>Find movies similar to your favorite one</p>", unsafe_allow_html=True)

st.write("---")

# Center the dropdown
col1, col2, col3 = st.columns([1,2,1])

with col2:
    selected_movie = st.selectbox(
        "🎥 Select a movie",
        new_df['title'].values
    )

# Button center
col4, col5, col6 = st.columns([1,2,1])

with col5:
    if st.button('🔍 Recommend'):
        recommendations = recommend(selected_movie)
        
        st.write("---")
        st.subheader("✨ Top Recommendations")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.markdown(f"**{recommendations[0]}**")
        with col2:
            st.markdown(f"**{recommendations[1]}**")
        with col3:
            st.markdown(f"**{recommendations[2]}**")
        with col4:
            st.markdown(f"**{recommendations[3]}**")
        with col5:
            st.markdown(f"**{recommendations[4]}**")

st.write("---")

# Footer
st.markdown("<p style='text-align: center;'>Built using Streamlit 🚀</p>", unsafe_allow_html=True)