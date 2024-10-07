import streamlit as st

st.markdown("<h2 style='text-align: center;'>Email Classification</h2>", unsafe_allow_html=True)

email_text = st.text_area("Paste your email text below to determine if it is spam or ham.", placeholder="Enter email text here...")

if "result" not in st.session_state:
    st.session_state.result = None
if "page" not in st.session_state:
    st.session_state.page = "Classification"

if st.button("Analyze"):
    if email_text:
        tfidf = st.session_state['tfidf']
        model = st.session_state['model']

        vec_text = tfidf.transform([email_text])

        y_pred = model.predict(vec_text)

        st.session_state.result = "Ham" if y_pred[0] == 0 else "Spam"
        st.success("Analysis Complete. Please proceed to see the result.")
    else:
        st.error("Please enter email text before clicking Analyze.")
if st.session_state.result:
    if st.button("Go to Result"):
        st.session_state.page = "Result"
        st.experimental_rerun()