import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as slt
import altair as alt

df1 = pd.read_csv('https://raw.githubusercontent.com/bmjames512/Hays_Co_PEV/main/2020PEV.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/bmjames512/Hays_Co_PEV/main/2018PEV.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/bmjames512/Hays_Co_PEV/main/2016PEV.csv')

Zip20 = df1.iloc[:,11]
Zip18 = df2.iloc[:,11]
Zip16 = df3.iloc[:,11]

Zip20S = Zip20.value_counts()
Zip18S = Zip18.value_counts()
Zip16S = Zip16.value_counts()

slt.title('Hays County Early Voting Data Analysis')
slt.write(
    "Use the Sliders to change the data displayed by the metric"
)
slt.bar_chart(Zip20S)
slt.bar_chart(Zip18S)
slt.bar_chart(Zip16S)