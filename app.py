import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="TP INF232 - Sommeil vs Notes", layout="wide")

st.title("TP INF232 : Analyse de la relation Sommeil / Notes")
st.write("Cette application Streamlit analyse l'impact du temps de sommeil sur les notes des étudiants.")

#Données d'exemple pour le TP
data = {
    'Heures_Sommeil': [4, 5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10],
    'Note_Moyenne': [8, 9.5, 11, 12, 14, 15, 16, 15.5, 14, 12.5]
}
df = pd.DataFrame(data)

st.subheader("1. Tableau des données")
st.dataframe(df)

st.subheader("2. Graphique : Corrélation Sommeil vs Notes")
fig, ax = plt.subplots()
ax.scatter(df['Heures_Sommeil'], df['Note_Moyenne'], color='blue')
ax.set_xlabel("Heures de sommeil par nuit")
data = {
'heures_sommeil': [4,5,6,6.5,7,7.5,8,8.5,9],
'note_moyenne': [8,10,11,12,14,15,16,15,14]
}
df = pd.DataFrame(data)
