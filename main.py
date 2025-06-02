import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'  # Получаем страницу, адрес
response = requests.get(url)  # передаем в функцию, так надо
soup = BeautifulSoup(response.text, 'lxml')  # используем конструктор, получаем текст ответа в переменную
# формат lxml

pages = soup.find('nav', class_='pagination')  # ищем навигацию по страницам
urls = []  # сюда засунем все ссылки позже
links = pages.find_all('a')  # ищем ссылки в найденной навигации

for link in links:
    # Проверяем, является ли текст ссылки числом
    if link.text.strip().isdigit():
        page_url = link.get('href')  # получаем значение атрибута href (адрес страницы)
        if page_url:  # если ссылка существует, добавляем её
            urls.append(page_url) #добавляем в список

unique_urls = list(set(urls))  # с помощью set удаляем дубликаты
unique_urls.append('')  # добавляем первую страницу вручную (она не отображается в пагинации)

n = 1  # начинаем счёт товаров с 1

for slug in unique_urls:
    new_url = url + slug  # собираем полный URL
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')  # нашли карточки товаров

    for i in items:
        itemName = i.find('h4').text.strip()
        itemPrice = i.find('h5').text.strip()
        print(f'{n}: {itemPrice} за {itemName}')  # красивый вывод
        n += 1  # увеличиваем счётчик после каждого товара
