
import streamlit as st 
from constant import *
import numpy as np 
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from graph_builder import *
#import tensorflow as tf
from streamlit_player import st_player

st.set_page_config(page_title='Yiping Chen\'s portfolio' ,layout="wide",page_icon='💃')

st.subheader('About me')
st.write(info['Brief'])

st.subheader('Career Timeline')
  
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

from constant import career_achievements
st.subheader('Career Achievements 🥇')
for position, achievements in career_achievements.items():
    st.markdown(f'<h3 style="font-size: 22px;"> As {position} </h3>', unsafe_allow_html=True)
    achievement_list = ''.join([f'<li>{achievement}</li>' for achievement in achievements])
    st.markdown(f'<ul>{achievement_list}</ul>', unsafe_allow_html=True)

linkedin_badge_html = """
<div class="badge-base LI-profile-badge" data-locale="zh_CN" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="yiping-chen-163002225" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://de.linkedin.com/in/yiping-chen-163002225?trk=profile-badge">Yiping Chen</a></div>
<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>"""
st.sidebar.markdown(linkedin_badge_html, unsafe_allow_html=True)

st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: chenerin1995@gmail.com')

pdfFileObj = open('photos/RESUME_YIPING_CHEN_copy.pdf', 'rb')
st.sidebar.download_button('download resume',pdfFileObj,file_name='RESUME_YIPING_CHEN_copy.pdf',mime='pdf')

photo_urls = [
    "photos/1.jpg",
    "photos/2.jpg",
    "photos/3.jpg",
    "photos/4.jpg",
    "photos/5.jpg",
    "photos/6.jpg",
    "photos/7.jpg",
    "photos/8.jpg"  
]

st.subheader('Me as a Photographer📷')  
num_cols = 3
num_rows = len(photo_urls) // num_cols + (len(photo_urls) % num_cols > 0)

grid = st.columns(num_cols)

# Display each photo in the grid
for i, photo_url in enumerate(photo_urls):
    row_index = i // num_cols
    col_index = i % num_cols
    with grid[col_index]:
        st.image(photo_url,  width=300)
