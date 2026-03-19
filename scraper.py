import requests 
from bs4 import BeautifulSoup
import pandas as pd
import time 

url="https://rss.dw.com/rdf/rss-de-all"

print("Connecting to DW . . .")
response=requests.get(url)


article_data=[]

if response.status_code == 200:
    print("Connection Successful! Fetching data . . . \n")
    #Parse the XML data using BeautifulSoup
    soup=BeautifulSoup(response.content, "xml")
    # Find all news items in the RSS feed
    new_items=soup.find_all("item")
    print(f"Found {len(new_items)} articles. Fetching the first 5 dor testing . . .\n")
    # Loop through the first 5 news items and print their details

    for item in new_items[:5]:
        title=item.title.text
        link=item.link.text

        print(f"Fetching content for : {title}")

        try:

            #Make a NEW request to the actual article page
            article_response = requests.get(link)

            if article_response.status_code==200:
                article_soup=BeautifulSoup(article_response.content, "html.parser")

                #All <p> tags in article
                paragraphs=article_soup.find_all("p")
                # Extract text from each paragraph and join them into one long string
                full_text= " ".join([p.text.strip() for p in paragraphs if p.text.strip()])

                article_data.append({
                    "Title":title,
                    "Link": link,
                    "Content": full_text
                })
            time.sleep(1)
        except Exception as e:
            print(f"Error Fetching {link}: {e}")

else:
    print(f"Erros occured! Status Code: {response.status_code}")


df=pd.DataFrame(article_data)
print("\n--- Scraping Completed! Here is your Data ---")
print(df.head())

df.to_csv("dw_articles.csv", index=False)
print("\n Data Successfully saved to dw_articles")