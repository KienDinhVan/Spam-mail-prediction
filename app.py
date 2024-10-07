import streamlit as st

#Page set up

home = st.Page(
    page='views/home.py',
    title='Home',
    icon=':material/home:',
    default=True
)

classification = st.Page(
    page='views/Classifier.py',
    title='Classification',
    icon=':material/dataset:'
)

result = st.Page(
    page='views/result.py',
    title='Result',
    icon=':material/check_circle:'
)

pg = st.navigation(pages=[home,classification,result])
pg.run()