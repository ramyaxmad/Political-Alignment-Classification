import requests
from bs4 import BeautifulSoup
import csv
import random

def get_forbes_political_links():
    url = "https://www.forbes.com/news/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed :(")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    article_links = set()

    political_keywords = ['biden', 'trump', 'congress', 'election', 'republican', 'democrat', 'senate']

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href'].lower()

        if href.startswith('https://www.forbes.com') and any(kw in href for kw in political_keywords):
            article_links.add(href.split('?')[0])

    return list(article_links)

def save_links_to_csv(links, filename='forbes_articles.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Article URL'])
        for link in links:
            writer.writerow([link])

if __name__ == '__main__':
    all_links = get_forbes_political_links()
    if not all_links:
        print("None found, yo")
    else:
        num_articles = min(15, len(all_links))
        random_links = random.sample(all_links, num_articles)
        save_links_to_csv(random_links)
        print("Articles Saved!!!")