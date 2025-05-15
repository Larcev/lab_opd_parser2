# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/' #Получаем страницу, адрес
response = requests.get(url) # передаем в функцию, так надо
soup = BeautifulSoup(response.text, 'lxml')  # используем конструктор, получаем текст ответа в переменную
# формат lxml
items = soup.find_all('div', class_='w-full rounded border')
for n, i in enumerate(items, start = 1):
    itemName = i.find('h4').text.strip()
    itemPrice = i.find('h5').text
#    print(f'{n}: {itemPrice} за {itemName}')


pages = soup.find('nav', class_='pagination')
urls = []
links = pages.find_all('a')

for link in links:
    # Проверяем, является ли текст ссылки числом
    if link.text.strip().isdigit():
        page_url = link.get('href')
        # Добавляем полный URL, если он не None
        if page_url:
            urls.append(page_url)

unique_urls = list(set(urls))

for slug in unique_urls:
    new_url = url + slug  # Собираем полный URL
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')
    for i in items:
        n += 1
        itemName = i.find('h4').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemPrice} за {itemName}')