import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

st.title('Penguins 데이터셋을 이용한 시각화 예제')

iris = pd.read_csv('data/penguins.csv')
st.write(iris.head())

x_var = st.selectbox('X축에 사용할 변수는?',
                     ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
y_var = st.selectbox('Y축에 사용할 변수는?',
                     ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])

