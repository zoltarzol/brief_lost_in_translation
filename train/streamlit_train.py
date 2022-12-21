import streamlit as st
import plotly.express as px
from streamlit import multiselect
import folium
import pandas as pd






#Charger vos données dans un dataframe Pandas.
#  Vous devrez peut-être nettoyer vos données pour vous assurer 
# qu'elles sont prêtes à être utilisées dans un graphique.
st.write("question 1 ")





st.write("question 2")
# Afficher l’évolution du nombre d’objets perdus à l’aide d’un plotly 
# sur la période 2016-2021. 
# On peut choisir d’afficher ou non certains types d’objet
liste_objet = ['Tous', 'Vêtements', 'Bijoux', 'Livres', 'Autres']
selected_object_types = multiselect('Type d\'objet:', liste_objet)
# if selected_object_types:
#   df_objet = df[df['type'].isin(selected_object_types)]

#fig = px.bar(df_objet, x='year', y='num_lost', title='Evolution du nombre d\'objets perdus')
#st.plotly_chart(fig)













#Afficher une carte de France avec le nombre d’objets perdus 
# en fonction de la fréquentation de voyageur de chaque région. 
# Possibilité de faire varier par année et par type d’objets
st.write("question3")

#Nombre d'objets perdus (par exemple, le nombre d'objets perdus dans chaque région)
#Année (si vous souhaitez pouvoir faire varier l'affichage par année)
#Type d'objet (si vous souhaitez pouvoir faire varier l'affichage par type d'objet)
liste_annee = ['Toutes', 2016, 2017, 2018, 2019, 2020, 2021]
liste_objet2 = ['Tous', 'Vêtements', 'Bijoux', 'Livres', 'Autres']
selected_year = multiselect('annee_choisi:', liste_annee)
selected_object_types2 = multiselect('Type d\'objet:', liste_objet2,key='object_types')



#if selected_year != 'Toutes':
#    df = df[df['year'] == year]
#if selected_object_types2 != 'Tous':
#    df = df[df['type'] == object_type]







# Nombre de voyageurs (par exemple, le nombre de personnes ayant visité chaque région)

df_carte = pd.DataFrame({'lat': [48.85, 43.1, 42.7, 48.9, 43.7],
                   'lon': [2.35, 1.44, 1.5, 2.7, 7.1],
                   'region': ['Ile-de-France', 'Languedoc-Roussillon', 'Provence-Alpes-Côte d\'Azur', 'Rhône-Alpes', 'Bretagne'],
                   'nb_voyageurs': [1234, 567, 891, 123, 456]})

# Tracer la carte de France en utilisant la fonction `go.Choropleth` de Plotly
fig = px.choropleth(df_carte,
                    title='Nombre de voyageurs par région',
                    range_color=[500, 1500],
                    center={'lat': 46.5, 'lon': 2.5},
                    width=800,
                    height=800,
                    projection='azimuthal equidistant',
                    locations = ["France"],
                    locationmode = 'country names',
                    scope='europe')

# voir comment faire avec Folium 


# Affichez la carte dans votre streamlit en utilisant la fonction `plotly_chart` de streamlit
st.plotly_chart(fig)



#for i in range(0, len(df)):
#    folium.CircleMarker(
#        location=[df.iloc[i]['lat'], df.iloc[i]['lon']],
#       radius=5,
#       color='#3186cc',
#        fill=True,
#       fill_color='#3186cc'
#    ).add_to(m)

