import pandas as pd
import spacy

print("Loading the German NLP model. . . ")

# Load the German language model

nlp=spacy.load("de_core_news_sm")

print("Reading the scraped data from CSV . . .")

df=pd.read_csv("dw_articles.csv")


def clean_text(text):
    #Pass the text through the Spacy NLP pipeline

    doc=nlp(str(text))

    clean_words=[]

    for token in doc:
        if not token.is_punct and not token.is_stop and not token.is_space:
            #Lemma (Dictionary Form)
            clean_words.append(token.lemma_.lower())

    return " ".join(clean_words)

print("Cleanin` the text data. . .(This might take a few seconds)")

#Apply out cleanin function to the entire 'Content' columns
df["Cleaned_Content"] = df["Content"].apply(clean_text)

print("Saving the cleaned data to a new file . . .")

df.to_csv("dw_articles_clean.csv", index=False)

print("\n --- Done ! Here is a comparison for the first article ---")
print(f"Original:\n {df['Content'].iloc[0][:150]}...\n")
print(f"Cleaned:\n {df['Cleaned_Content'].iloc[0][:150]}...")
