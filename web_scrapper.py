import requests
from bs4 import BeautifulSoup

def scrape_news_articles(url):
    """
    Scrape news articles from the specified URL.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content
        print(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all article elements
        articles = soup.find_all('li', class_='news-article-list')
        # Extract headlines and article URLs
        news_articles = []
        for article in articles:
            headline = article.find('h2').text.strip()
            print(headline)
            article_url = article.find('a')['href']
            news_articles.append({'headline': headline, 'url': article_url})
        return news_articles
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Example URL for scraping news articles (replace with your desired source)
    url = 'https://www.kenyans.co.ke/news'
    print(url)
    articles = scrape_news_articles(url)
    for article in articles:
        print(article)



# API Key  = on3mdncBEbCllvqGyvofJ7Sd0
# API Key Secret=  IrANKAQif8HqmU2k9s8byt8cFUMbWYUcLImwpFd3lHKQ0J3llv
# Bearer Token = AAAAAAAAAAAAAAAAAAAAABgTngEAAAAAg2DzfNhfJko8QWu%2FvoXDOjPeYt4%3DzE8fOoVuAgEC2d9iHZ2cPR6MG1g6PZMPAJMAwR4NVb0ePtsg53
# Access Token  = 1489158343927156739-xp6XLz04J3NyNaxzMR9VBB3NaNRc3T
# Access Token Secret = mloNH41ztVhDuGDyxfDQGDSo6Z19LpRt7ZnIshf89RgOB
# Client Id = SmlMQ1B3RWYtMndKb0hMVjljNzY6MTpjaQ
# Client Secret = cp1p0bb_3eUv7nNLe-lePvSLzBZLPNA88SvCXJ70oeKqcE3f-i