import streamlit as st
import pickle
import pandas as pd

# ----------------- Load Data -----------------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_idx = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].original_title)
    return recommendations


# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Mode selector (Light / Dark)
mode = st.sidebar.radio("🌗 Choose Mode:", ["Light", "Dark"])

# Dynamic CSS for background + theme
if mode == "Dark":
    background_color = "#1e1e1e"
    text_color = "#f5f5f5"
    card_color = "#333333"
else:
    background_color = "#f5f5f5"
    text_color = "#222222"
    card_color = "#ffffff"

st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            color: {text_color};
        }}
        .card {{
            background-color: {card_color};
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }}
        .card:hover {{
            transform: scale(1.05);
            box-shadow: 0px 6px 16px rgba(0,0,0,0.3);
        }}
        h1 {{
            color: #FFD700;
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:{text_color}; font-size:18px;'>Find movies similar to your favorites instantly!</p>", unsafe_allow_html=True)

# Movie selector
movies_list = movies['original_title'].values
st.markdown("### 🔎 Pick a movie:")
option = st.selectbox("", movies_list)

# Recommend button
if st.button("✨ Recommend"):
    recommended = recommend(option)

    st.markdown("## 🎥 Top 5 Recommendations")
    cols = st.columns(5)

    for idx, movie in enumerate(recommended):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="card">
                    <h4>{movie}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
