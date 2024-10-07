import streamlit as st

# Page configuration
st.markdown("<h2 style='text-align: center;'>Classification Result</h2>", unsafe_allow_html=True)
# col1, col2, col3 = st.columns([1,0.4,1])
# with col2:
#     st.image("assets/piechart.png", caption="", use_column_width=True)

# Display the result if available in session state
if st.session_state.result:
    col1, col2, col3 = st.columns([1, 0.4, 1])
    with col2:
        st.image("assets/piechart.png", caption="", use_column_width=True)
    classification = st.session_state.result
    st.markdown(f"<h3 style='text-align: center;'>The input text has been classified as {classification}.</h3>", unsafe_allow_html=True)
else:
    # st.write("No analysis has been done yet. Please proceed to the classification page first.")
    st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; height: 50px'>
            <div style='text-align: center;'>
                <p>No analysis has been done yet. Please proceed to the classification page first.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)