# 📰 DW Nachrichten Analysator (DW Haber Analizörü)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dw-news-analyzer.streamlit.app/)

Willkommen zu meinem NLP- und Machine-Learning-Projekt! (NLP ve Makine Öğrenmesi projeme hoş geldiniz!) 🚀

Diese interaktive Webanwendung kratzt (scraped) automatisch die neuesten Artikel von der **Deutsche Welle (DW)** Website, analysiert die deutschen Texte mit Natural Language Processing (NLP) und gruppiert sie mithilfe von Machine Learning in sinnvolle Kategorien.

## ✨ Features (Özellikler)
* **Automatisches Web Scraping:** Zieht die neuesten deutschen Nachrichten von DW.com.
* **NLP Textbereinigung:** Entfernt Stoppwörter und bereinigt den Text mit `spaCy` (de_core_news_sm).
* **K-Means Clustering:** Gruppiert Artikel automatisch in Themen wie "Wirtschaft", "Politik" oder "Internationale Konflikte" mit `scikit-learn`.
* **Interaktive UI:** Eine benutzerfreundliche Oberfläche, erstellt mit `Streamlit`.
* **Wortwolken (WordClouds):** Visuelle Darstellung der am häufigsten verwendeten Wörter pro Cluster.

## 🛠️ Technologien (Teknolojiler)
* **Python 3.12**
* **Streamlit** (Frontend & Deployment)
* **scikit-learn** (Machine Learning / TF-IDF & K-Means)
* **spaCy** (Natural Language Processing)
* **Pandas** (Data Manipulation)
* **BeautifulSoup & Requests** (Web Scraping)
* **Matplotlib & WordCloud** (Datenvisualisierung)

## 🚀 Live-Demo
Klicke auf den Badge oben oder besuche die App direkt hier:  
👉 **[DW News Analyzer auf Streamlit](https://dw-news-analyzer.streamlit.app/)**

## 💻 Lokal ausführen (Yerel Bilgisayarda Çalıştırma)
Wenn du dieses Projekt auf deinem eigenen Computer ausführen möchtest:

1. Repository klonen:
   ```bash
   git clone [https://github.com/BoraAydoan/dw-news-analyzer.git](https://github.com/BoraAydoan/dw-news-analyzer.git)
