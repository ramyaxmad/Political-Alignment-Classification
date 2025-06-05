import requests
from bs4 import BeautifulSoup
import csv
import random

def get_bbc_politics_article_links():
    base_url = "https://www.bbc.com/"
    # politics_url = f"{base_url}/politics"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        print("Failed, foo!")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    all_links = set()

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/'):
            full_url = base_url + href
        elif href.startswith('http'):
            full_url = href
        else:
            continue

        # /202 to get recent years da 2020's
        if '/news/articles/' in full_url:
            all_links.add(full_url)

    return list(all_links)

def save_links_to_csv(links, filename='bbc_articles.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Article URL'])
        for link in links:
            writer.writerow([link])

if __name__ == '__main__':
    all_links = get_bbc_politics_article_links()
    if not all_links:
        print("links gotten!")
    else:
        num_articles = min(15, len(all_links))
        random_links = random.sample(all_links, num_articles)
        save_links_to_csv(random_links)
        print(f"Saved {len(random_links)} in the .csv")
