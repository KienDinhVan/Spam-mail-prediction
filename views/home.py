import streamlit as st
import pickle

# Load the vectorizer, label encoder, and trained model
with open('tfidf_vectorizer.pkl', 'rb') as tfidf_file:
    tfidf = pickle.load(tfidf_file)

with open('spamham_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoder.pkl', 'rb') as encod_file:
    encod = pickle.load(encod_file)

# Store the loaded models in Streamlit session state for reuse in other pages
if 'tfidf' not in st.session_state:
    st.session_state['tfidf'] = tfidf
if 'model' not in st.session_state:
    st.session_state['model'] = model

# Streamlit configuration
st.set_page_config(page_title="Spam Mail Classifier", layout="wide")

# App title
st.markdown("<h1 style='text-align: center;'>Spam Mail Classifier</h1>", unsafe_allow_html=True)

# Sidebar title
st.sidebar.markdown("# Kien Dinh Van")

# Center the welcome text using custom HTML
st.markdown("<h3 style='text-align: center;'>Welcome to Spam Mail Classifier</h3>", unsafe_allow_html=True)
st.markdown("""
    <div style='display: flex; justify-content: center; align-items: center; height: 100px'>
        <div style='text-align: center;'>
            <p>This is a tool to classify emails as spam or ham using a pre-trained model.</p>
            <p>Navigate to 'Classification' page from the sidebar to classify your emails.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
