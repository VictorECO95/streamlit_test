import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("TITANIC")
st.header("Ejemplo Titanic")

df=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')

st.dataframe(df)
st.subheader("Info Basica")
col1,col2,col3 =st.columns(3)
col1.metric("Filas",df.shape[0])
col2.metric("Columnas",df.shape[1])
col3.metric("Nulos Totales",df.isnull().sum().sum())

st.subheader("Nulos")
st.write("Nulos",df.isnull().sum())

