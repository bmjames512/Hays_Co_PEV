import numpy as np
import pandas as pd
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

# Average Age of EPV
EPV20 = df1.iloc[:,5].mean()
EPV18 = df2.iloc[:,5].mean()
EPV16 = df3.iloc[:,5].mean()

EC = {'2016': EPV16, '2018': EPV18, '2020': EPV20}

EPVFrame = pd.DataFrame.from_dict(EC, orient='index')

slt.title('Hays County Early Voting Data Analysis')

Cities = np.array(['Coming Soon','Wimberley', 'Kyle', 'Buda', 'San Marcos'])

db1, db2 = slt.beta_columns(2)
with db1:
    year = slt.radio('Year', ['Empty', 2016, 2018, 2020])
with db2:
    sd1 = slt.slider('Min Age',min_value=18,max_value=100,value=50)
    sd2 = slt.selectbox('City', Cities)


if year=='Empty':
    slt.write('')
if year==2016:
    slt.header('2016 EV Data')
    slt.bar_chart(Zip16S)
if year==2018:
    slt.header('2018 EV Data')
    slt.bar_chart(Zip18S)
if year==2020:  
    slt.header('2020 EV Data')
    slt.bar_chart(Zip20S)


# -----------------------------------
# Joining Tables

# Add Yr2020
Lb1 = pd.DataFrame(df3.copy())
ar1 = np.zeros((5303,1))
ar1[:] = True
print(ar1)
yr1= pd.DataFrame(data=ar1, columns=["2016EV"])
Lba1 = Lb1.join(yr1, how="outer")

# Add Yr2018
Lb2 = pd.DataFrame(df2.copy())
ar2 = np.zeros((5245,1))
ar2[:] = True
yr2= pd.DataFrame(data=ar2, columns=["2018EV"])
Lba2 = Lb2.join(yr2, how="outer")

# Add Yr2020
Lb3 = pd.DataFrame(df1.copy())
ar3 = np.zeros((10960,1))
ar3[:] = True
yr3= pd.DataFrame(data=ar3, columns=["2020EV"])
Lba3 = Lb3.join(yr3, how="outer")

#Append to All - dfc2016
dfc2018 = pd.merge(Lba3, Lba2, how='outer')
dfc2016 = pd.merge(dfc2018, Lba1, how='outer')

# -----------------------------------

bigchart= dfc2016[dfc2016["Age"] > sd1]

AgeCV = pd.Series(bigchart.iloc[:,5])
slt.bar_chart(AgeCV.value_counts(normalize=True))


slt.title('1. Primary Voters Became Younger in 2020')
slt.write(
    'Analysis of the data sources show that the age of the primary voter increased, but only marginally in 2018. '
    'According to the Analyst Group, a measurement center for Elections Data, Texas elections experience a 10 point gap between the two'
)
slt.line_chart(EPVFrame)
slt.markdown(
    'In 2016, the average age of a Dem Primary Voter was **56.5** years old, but in 2018 it rose to **56.7**, and then in 2020 it dipped down to **50** years old.'
)

col1, col2, col3 = slt.beta_columns(3)
with col1:
    slt.header("2016 Age Stats")
    slt.write (df3.iloc[:,5].describe())
with col2:
    slt.header("2018 Age Stats")
    slt.write (df2.iloc[:,5].describe())
with col3:
    slt.header("2020 Age Stats")
    slt.write (df1.iloc[:,5].describe())


Zip20Top = Zip20S.sort_values(ascending=False).head(5)
Zip18Top = Zip18S.sort_values(ascending=False).head(5)
Zip16Top = Zip16S.sort_values(ascending=False).head(5)



slt.title('2. Top Voting Zip Codes are Fairly Predictable')

col4, col5, col6 = slt.beta_columns(3)
with col4:
    slt.header("2016 Top Zips")
    slt.dataframe(Zip16Top)
with col5:
    slt.header("2018 Top Zips")
    slt.dataframe(Zip18Top)
with col6:
    slt.header("2020 Top Zips")
    slt.dataframe(Zip20Top)
