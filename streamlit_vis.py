import streamlit as st
import plotly.express as px
from streamlit import multiselect
import folium
import pandas as pd

df = pd.read_csv('data_objet_and_freq.csv')
df['date_heure_decouverte_OT'] = pd.to_datetime(df['date_heure_decouverte_OT'])
df['date_heure_restitution_OT'] = pd.to_datetime(df['date_heure_restitution_OT'])



st.write("question 1 ")
# copier ce qui a dans le jupyter 
# Load the data into a dataframe
# Load the data into a dataframe
df = pd.read_csv('data_objet_and_freq.csv')

# Convert the "date_heure_decouverte_OT" column to datetime
df['date_heure_decouverte_OT'] = pd.to_datetime(df['date_heure_decouverte_OT'])

# Group the data by weekly intervals and count the number of rows in each group
question_1 = df.groupby(pd.Grouper(key='date_heure_decouverte_OT', freq='W')).size()

# Convert the index to a list of strings
#x = question_1.index.strftime('%Y-%m-%d').tolist()
question_1.index = pd.to_datetime(question_1.index)
# Create a bar chart
st.bar_chart(question_1)
# completement a modifier 



st.write("question 2")
# Afficher l’évolution du nombre d’objets perdus à l’aide d’un plotly 
# sur la période 2016-2021. 
# On peut choisir d’afficher ou non certains types d’objet
liste_objet = list(df['type_OT'].unique())
liste_objet.insert(0,'Tous')
selected_object_types = multiselect('Type d\'objet:', liste_objet)

if selected_object_types:
    df_objet = df[df['type_OT'].isin(selected_object_types)]
    question_2 = df_objet.groupby(pd.Grouper(key='date_heure_decouverte_OT', freq='Y')).count()
    fig = px.bar(question_2, x= question_2.index, y='type_OT', title='Evolution du nombre d\'objets perdus')
    st.plotly_chart(fig)

else:
    st.write("Vous n'avez rien  choisi")
# transformer an_2020 pour choisir le total , par le temps , bref des erreurs partout , delimiter l'annee comme montré p
# chat GPT










#Afficher une carte de France avec le nombre d’objets perdus 
# en fonction de la fréquentation de voyageur de chaque région. 
# Possibilité de faire varier par année et par type d’objets
st.write("question3")

#Nombre d'objets perdus (par exemple, le nombre d'objets perdus dans chaque région)
#Année (si vous souhaitez pouvoir faire varier l'affichage par année)
#Type d'objet (si vous souhaitez pouvoir faire varier l'affichage par type d'objet)
liste_annee = ['Toutes', 'an_2016', 'an_2017', 'an_2018', 'an_2019', 'an_2020', 'an_2021']
selected_year = multiselect('annee_choisi:', liste_annee)
selected_object_types2 = multiselect('Type d\'objet:', liste_objet,key='object_types')


# Load the data into a dataframe
# Load the data into a dataframe
df_carte = pd.read_csv('data_objet_and_freq.csv')

# Convert the "date_heure_decouverte_OT" column to datetime
df_carte['date_heure_decouverte_OT'] = pd.to_datetime(df_carte['date_heure_decouverte_OT'])

# Extract the year from the datetime objects
df_carte['year'] = df_carte['date_heure_decouverte_OT'].dt.year

# Filter the data for the selected years
df_carte = df_carte[df_carte['year'].isin(selected_year)]

# Group the data by region and count the number of rows in each group
df_grouped = df_carte.groupby('region_y').agg({
    'an_2016': 'sum',
    'an_2017':  'sum',
    'an_2018': 'sum',
    'an_2019': 'sum',
    'an_2020': 'sum',
    'an_2021': 'sum',
    'type_OT': 'count'})

regions = df_carte.groupby('region_y').size()

# Create a choropleth map
fig = px.choropleth(regions, title="Lost Items by Region")


fig = px.choropleth(df_grouped, title="Lost Objects per Traveler by Region", color='type_OT')

# Display the map in the Streamlit app
st.plotly_chart(fig)
# this doesn't work as planned 












