import streamlit as st
import pandas as pd

#Titel und Beschreibung der Webseite

st.title("Dw Nachrichten Analysator")
st.write("Diese App zeigt  die neuesten Artikel von Deutsche Welle, die durch" \
"Kübstliche Intelligenz automatisch in Themen gruppier wurden.")
  

#Data laden(mit Catche, damit es schnell bleibt)

@st.cache_data
def load_data():
    return pd.read_csv("/Users/boraa/Desktop/dw_project/dw_articles_clustered.csv")

df=load_data()

#1. Die gesamte Tabelle anzeigen
st.subheader("📰 Alle gesammelten Artikel")

cluster_names={
    0: "Wirtschaft & Finanzen",
    1: "Internationale Konflikte",
    2: "Politik & Gesellschaft"
}
#Wir zeigen nur die wichtigsten Spalten in der interaktiven Tabelle 
st.dataframe(df[['Title','Link','Cluster']], width='stretch')

st.divider()

#2. Ein interaktiver Filter für den Benutzer
st.subheader("🔍 Artikel nach Themen filtern")

#Ein Dropdown-Menu erstellen, das die schön Namen anzeigt
selected_name= st.selectbox("Wahle ein Thema aus:", list(cluster_names.values()))



#Ein Dropdown-Menu erstellen
selected_cluster=list(cluster_names.keys())[list(cluster_names.values()).index(selected_name)]


#Die Daten bausirerend auf der Auswahl filtern
filtered_df=df[df['Cluster']==selected_cluster]

#Das gefilterte Ergenis anzeigen
st.write(f"Du siehst jetzt nur die Artikel aus **Cluster {selected_cluster}**:")

st.dataframe(
    filtered_df[['Title', 'Link']], 
    column_config={
        "Link": st.column_config.LinkColumn(
            "Original Artikel",  # Der Name der Spalte (Sütun adı)
            help="Klicke hier, um den Artikel auf DW.com zu lesen", # Tooltip beim Drüberfahren
            display_text="Lies den Artikel 🔗" # Der Text, der statt der URL angezeigt wird (Görünen metin)
        )
    },
    hide_index=True, # Versteckt die unnötigen Zahlen (0, 1, 2...) am Rand
    use_container_width=True
)

st.table(filtered_df[['Title']])