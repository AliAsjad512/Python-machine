import requests
from bs4 import BeautifulSoup
import csv

def web_scraper(url, output_file='data.csv'):
    """Scrape website data and save to CSV"""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Scrape headlines
        data = []
        for article in soup.find_all('article')[:10]:
            title = article.find('h2').text.strip() if article.find('h2') else 'N/A'
            link = article.find('a')['href'] if article.find('a') else 'N/A'
            data.append([title, link])
        
        # Save to CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Link'])
            writer.writerows(data)
        
        print(f"Scraped {len(data)} items to {output_file}")
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

# Usage
web_scraper('https://news.ycombinator.com/', 'news.csv')