# 🎬 Movie Recommendation System

A simple and interactive **Movie Recommendation System** built with **Streamlit**, **Python**, and **Machine Learning**.  
It recommends 5 movies similar to the one selected by the user.  

---

## 🚀 Features
- 🎥 Recommends 5 similar movies instantly  
- 🌗 Light/Dark Mode toggle for better UI  
- 🎨 Stylish and interactive frontend using Streamlit  
- ⚡ Powered by cosine similarity & movie embeddings  

---

## 🛠️ Tech Stack
- **Frontend/UI** → [Streamlit](https://streamlit.io/)  
- **Backend** → Python  
- **ML/Data Handling** → Pandas, NumPy, Scikit-learn  
- **Pickle** → Used for saving preprocessed data (`movies.pkl`, `similarity.pkl`)  

---

## 📂 Project Structure

movie-recommender/

|--movie_recommender_system1-checkpoint.ipynb
│── app.py
│── movies.pkl
│── data/                # data can be downloaded from kaggle tmdb dataset
│   └── movies_metadata.csv
│   └── credits.csv
│── requirements.txt
│── README.md
 # NEW notebook for preprocessing/training



---

## ⚙️ Setup & Installation

1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

2️⃣ Create virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # for Mac/Linux
venv\Scripts\activate      # for Windows


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Run the Streamlit app

streamlit run app.py


5️⃣ Open in browser
Streamlit will give you a local URL, usually:

👉 http://localhost:8501

