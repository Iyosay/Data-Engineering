import requests 

url = "https://content.guardianapis.com/search?api-key=test&q=nigeria&from-date=2025-01-01&page-size=100"

response_API = requests.get(url)

print(response_API.status_code)

print(response_API)

get_data = response_API.json()

get_data.keys()

get_data['response'].keys()

get_data['response']['results']

data = get_data['response']

data['results']

article_urls = []

for article in data['results']:  
    urls = article['webUrl']  
    article_urls.append(urls) 

print(article_urls)

import pandas as pd

df = pd.DataFrame({'article_urls': article_urls})

print(df)

df.to_csv('article_urls.csv')
