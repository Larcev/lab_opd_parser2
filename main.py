
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/' #Получаем страницу, адрес
response = requests.get(url) # передаем в функцию
soup = BeautifulSoup(response.text, 'lxml')  # используем конструктор, получаем текст ответа в переменную
# формат lxml
items = soup.find_all('div', class_='w-full rounded border') # ищем все дивы с таким-то классом
#код ниже работает для вывода только одной страницы, вывод закомментирован
for n, i in enumerate(items, start = 1): # перебор из списка items, начинаем с 1, это для красивого вывода 
    itemName = i.find('h4').text.strip() 
    itemPrice = i.find('h5').text
#    print(f'{n}: {itemPrice} за {itemName}')  


pages = soup.find('nav', class_='pagination') #ищем остальные страницы 
urls = [] # сюда засунем все ссылки позже
links = pages.find_all('a') #ищем ссылки в найденных страницах

for link in links:
    # Проверяем, является ли текст ссылки числом
    if link.text.strip().isdigit(): #нам нужны числа, тоесть 1,2,3,4,5,6... на этом сайте так, ну и на других
        page_url = link.get('href') #добавлем href
        # Добавляем полный URL, если он не None
        if page_url:
            urls.append(page_url)

unique_urls = list(set(urls)) #с помощью set делаем множество, удаляя дубликаты(мн-ва хранят уникальные значения)
# потом снова в список с помощью list

for slug in unique_urls:
    new_url = url + slug  # Собираем полный URL
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, 'lxml') 
    items = soup.find_all('div', class_='w-full rounded border') #нашли что надо
    for i in items: # красиво выводим
        n += 1
        itemName = i.find('h4').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemPrice} за {itemName}') #красивый вывод
