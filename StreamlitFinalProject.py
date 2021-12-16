import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False)
st.image('Fortune 500 companies.jpg', width=700)
filename = 'Fortune_500_Corporate_Headquarters.csv'
df = pd.read_csv(filename)
intermitterdf = df.sort_values(['RANK'])
st.title("Fortune 500 Companies by Rank")
whoknows = pd.get_dummies(intermitterdf)
DataRank = int(st.sidebar.selectbox("Search Companies by Rank", whoknows['RANK'], key=1))
datainfo = whoknows.iloc[DataRank]
st.write('You selected the company with the Rank: ', DataRank+1)
st.write(datainfo)

intermitterdfpart2 = df.sort_values(['FID'])
st.title("Fortune 500 Companies by FID")
whoknowspart2 = pd.get_dummies(intermitterdfpart2)
DataRankpart2 = int(st.sidebar.selectbox("Search Companies by FID", whoknowspart2['FID'], key=2))
datainfopart2 = whoknowspart2.iloc[DataRankpart2]
st.write('You selected the company with the FID: ', DataRankpart2+1)
st.write(datainfopart2)
st.title("Graph of Profits")
numbaone = int(st.sidebar.slider("Range for Profits Graph (starts with 0)", min_value=0, max_value=501, step=1, key=3))
#numbatwo = int(input("Please input the range for results you want to see (0=1st position) :"))
newdf = df[df['RANK'] < numbaone]
xs = newdf['RANK']
ys = newdf['PROFIT']
plt.bar(xs, ys, width=1, align='center')
plt.xlabel("Company Names")
plt.ylabel("Profits")
plt.title("Profits")
st.pyplot()

st.title("Map of Fortune 500 Companies")
newdf = df.rename(columns={'LATITUDE': 'latitude', 'LONGITUDE': 'longitude'})
mapdf = pd.DataFrame(newdf, columns=['longitude', 'latitude', 'NAME'])
st.map(mapdf)
