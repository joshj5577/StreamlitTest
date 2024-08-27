
# Some libraries

import streamlit as st
from streamlit_observable import observable
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import sshtunnel
import paramiko
import pymysql
import base64
import requests
import bar_chart_race as bcr

## Plot style, you can change it.
sns.set()
## In this case we chosea default seaborn style.

# ---------------------------------------Functions--------------------------------------- #

## Functions can be in other script.py

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<div style="text-align: left;"><img src="data:image/svg+xml;base64,%s"/></div>' % b64
    st.sidebar.write(html, unsafe_allow_html=True)

def score_hist(df_aux,activity_id,x='score'):
    fig, ax = plt.subplots(1,1,figsize=(2.7,2.7))
    label = 'n = '+str(len(df_aux))
    p = sns.histplot(data=df_aux,x=x,label=label,color='#00ABC8',stat="probability",ax=ax)
    p.set_title("\n Distribution of users's score of activity: "+activity_id+"\n",fontsize = 5)
    p.set_ylabel("Probability", fontsize = 5)
    p.set_xlabel("Score", fontsize = 5)
    p.tick_params(labelsize=3)
    ax.legend(loc='best',prop={'size': 6})
    ax.axis(xmin=0,xmax=1)
    st.pyplot(fig)

# ---------------------------------------Functions--------------------------------------- #


# --------------------------------------Create body-------------------------------------- #

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 325px;
        background-color: rgb(240,250,250);
    }
    </style>
    """,
    unsafe_allow_html=True,
)
url = "https://www.neuronup.com/wp-content/uploads/2021/07/logo-neuronup-core.svg"
r = requests.get(url) # Get the webpage
svg = r.content.decode() # Decoded response content with the svg string
render_svg(svg) # Render the svg string
st.sidebar.markdown("<h1 style='text-align: left; font-size: 35px;\
color:#636569;'>Hello Streamlit</h1>", unsafe_allow_html=True)


st.sidebar.markdown("#### Sample of data analysis visualization")
select_event = st.sidebar.selectbox('Choose one option', ['Option',\
'Hello streamlit','Overall data analysis','Activity analysis'])

# --------------------------------------Create body-------------------------------------- #



# ----------------------------------------options---------------------------------------- #

# --------------------------------------------------------------------------------------- #
## Space reserved to show the different options, together with their graphs, of the analysis.
## You can also define your own display functions.
# --------------------------------------------------------------------------------------- #

##    ------------------------------For overall analysis-----------------------------    ##

if select_event == 'Overall data analysis':
    st.markdown("<h1 style='text-align: center; font-size: 40px;\
    color:#636569;'>Work In Progress</h1>", unsafe_allow_html=True)


##    -----------------------------For activity analysis-----------------------------    ##

if select_event == 'Activity analysis':
    select_event2 = st.sidebar.selectbox('Choose an activity id', ['Activity id','355'])
    if select_event2 != 'Activity id':

        # Load dataframe of activity 
        df = pd.read_csv('sample_data/activity_'+select_event2+'.csv')

        select_event3 = st.sidebar.selectbox('Choose one visualisation\
        of activity: ' + select_event2, ['List of visualizations',\
        'Display result variables',"Histogram os user's score"])
        
        if select_event3 == "Histogram os user's score":

            st.markdown("<h1 style='text-align: center; font-size: 40px'>\
            Histogram of results</h1>", unsafe_allow_html=True)

            st.markdown("<p style='text-align: center; font-size: 20px;'>\
            Here is an example of how to display a graph of the average score\
            of users in this activity.</p>", unsafe_allow_html=True)

            df_aux = df.groupby('patient_id').mean()

            # To show histogram of data
            score_hist(df_aux,select_event2)

            st.write("")

            st.markdown("<p style='text-align: center; font-size: 20px;'>\
            Note that in this activity users tend to get good results.</p>",\
            unsafe_allow_html=True)
        
        # Show result variables
        if select_event3 == 'Display result variables':
            st.markdown("<h1 style='text-align: center; font-size: 40px'>\
            Work in progress!</h1>", unsafe_allow_html=True)

##    ------------------------------Sample of streamlit------------------------------    ##

elif select_event == 'Hello streamlit':


    st.markdown("<h1 style='text-align: center; font-size: 40px'>\
    Hello streamlit</h1>", unsafe_allow_html=True)

    st.markdown("</br>", unsafe_allow_html=True)

    st.markdown("On this page I will show you some examples of how streamlit works.</p>",\
    unsafe_allow_html=True)

# ----------------------------------------options---------------------------------------- #
