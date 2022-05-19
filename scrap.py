from logging import exception
import requests, openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Rated Movies Scraping'
print(excel.sheetnames)
sheet.append(['Film Ranking','Film Name', 'Release Date', 'Film Rating'])
try:
    html_page = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(html_page.text, 'html.parser')
    films_all = soup.find('tbody', class_="lister-list").find_all('tr')
    
    count = 0
    for i in films_all:
        Film_name = i.find('td', class_='titleColumn').a.text
        count = count+1
        Film_rank = count
        date = i.find('td', class_='titleColumn').span.text.strip('()')
        Film_rating = i.find('td', class_='ratingColumn').strong.text
        
        sheet.append([Film_rank, Film_name, date, Film_rating])

except Exception as e:
    print(e)

excel.save('Movie Scraping.xlsx')