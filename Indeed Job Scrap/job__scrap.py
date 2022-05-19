
import requests
from bs4 import BeautifulSoup

try:
    def scraping(page):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
        url = f'https://www.indeed.com/jobs?q=python%20developer&l=london&start={page}'
        source = requests.get(url, headers)

        soup = BeautifulSoup(source.content, 'html.parser')
        return soup

except Exception as e:
    print(e)

def pull_out(soup):
    tds = soup.find_all('td', class_="resultContent")
    for i in tds:
        title = i.find('a').text.strip()
        company = i.find('span', class_='companyName').text.strip()
        try:
            salary = i.find('span', class_="estimated-salary").span.text

        except:
            salary = ''
        
        return title
a = scraping(0)
print(pull_out(a))
