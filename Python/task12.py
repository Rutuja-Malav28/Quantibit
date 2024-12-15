# Scrape and print news headlines. 
# Input: URL of a news website.                               
# Output: 
# 1. Headline 1 
# 2. Headline 2 
# 3. Headline 3 


import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        for index, headline in enumerate(headlines, start=1):
            headline_text = headline.get_text(strip=True)
            if headline_text:
                print(f"{index}. {headline_text}")
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")


url = 'https://www.bbc.com/news'  
scrape_headlines(url)
