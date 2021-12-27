#import library
import pandas as pd
import plotly.graph_objects as go
import pathlib
import numpy as np
import streamlit as st


#data
path1='E:/Python/eddies/ioe2022/p1hari.csv'
path2='E:/Python/eddies/ioe2022/p2hari.csv'
path3='E:/Python/eddies/ioe2022/p3hari.csv'
data_dir5='E:/Python/eddies/ioe2022/informasimodel2.csv'

df1=pd.read_csv(path1)
df2=pd.read_csv(path2)
df3=pd.read_csv(path3)
im=pd.read_csv(data_dir5)

#fungsi plot interaktif
def line_plot2(df,title):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(name='Predicted',
            x=df['hours'],
            y=df['Predicted'],
            line = dict(color='blue', width=4))
        )
    fig.add_trace(
        go.Scatter(name='Observation',
            x=df['hours'],
            y=df['Observation'],
            line = dict(color='red', width=4))
            )
  
    fig.update_layout(title=title,
                  title_x=0.5,
                  font=dict(
        size=18,
        color="black"),
                   xaxis_title='Time',
                   yaxis_title='Magnitude(m/s)',
                  width=900,
                  height=500,
                  legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01)
                      )
    fig.update_xaxes(title_text='Dates')
    fig.update_yaxes(range=[0,2.5],title_text='SWH (m)')
    fig.show()
    col2.plotly_chart(fig)
    

display = ("Prediction for 1 days", "Prediction for 2 days","Prediction for 3 days")
options = list(range(len(display)))
    
st.set_page_config(layout="wide")
st.sidebar.markdown("## SWH Prediction")
with st.sidebar:
  sp=st.selectbox("Choose you want to know", ["Prediction for 1 days", "Prediction for 2 days", "Prediction for 3 days"])
    
st.markdown("<h1 style='text-align: left; color: black; font-size:40px'>Dashboard for Ocean Wind and Wave Data on Indonesia Fisheries Management Area 711</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left; color: black; font-size:18px'>WPP-RI 711 is a fisheries management area in Indonesia consisted of Natuna Sea, Karimata Strait, and some part of South China Sea.</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: black; font-size:40px'></h3>", unsafe_allow_html=True)

col1,col2 = st.columns((1,2))
col1.markdown("<h1 style='text-align: left; color: black; font-size:40px'></h1>", unsafe_allow_html=True)
col1.markdown("<p style='text-align: left; color: black; font-size:24px'>Model Information</p>", unsafe_allow_html=True)
col1.dataframe(im, width=1000, height=1800)

if sp=="Prediction for 1 days":
  title="Prediction for 1 Days"
  line_plot2(df1,title)  

elif sp=="Prediction for 2 days":
  title="Prediction for 2 Days"
  line_plot2(df2,title)
  
elif sp=="Prediction for 3 days":
  title="Prediction for 3 Days"
  line_plot2(df3,title)

st.set_option('deprecation.showPyplotGlobalUse', False)

