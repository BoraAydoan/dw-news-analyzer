import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

print("Lese die sauberen Date . . .")
df=pd.read_csv("dw_articles_clean.csv")
df=df.dropna(subset=['Cleaned_Content'])

print("Text wird in Zahlen umgewandelt (TD-IDF). . .")

#Wir nehmen nur die 1000 wichtigsten Woter, um das Modell effizient zu halten
vectorizer = TfidfVectorizer(max_features=1000)

X=vectorizer.fit_transform(df['Cleaned_Content'])

print("K-means Modell traniert (3 Cluster)")

kmeans=KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster']=kmeans.fit_predict(X)

print("Spreichere die Ergebnisse . . . ")
df.to_csv("dw_articles_clustered.csv", index=False)

print("\n--- FERTIG! Hier sind die ersten Artikel mit ihren Clustern ---")

print(df[['Title','Cluster']].head())

print("\n--- Top 10 WÖRER PRO CLUSTER ---")

order_centroids=kmeans.cluster_centers_.argsort()[:,: : -1]

terms=vectorizer.get_feature_names_out()

for i in range(3):
    print(f"Cluster {i}:")

    top_words=[terms[ind] for ind in order_centroids[i,:10]]
    print(", ".join(top_words))
    print("-" * 30)