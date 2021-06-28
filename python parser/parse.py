from bs4 import BeautifulSoup
import requests
import csv

limit = 0
limitStep = 24
with open('conditions.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Название кондиционера', 'Цена'])
while(True):
    linkToConditions = f'https://kurs-klimat.ru/katalog/konditsionery-nastennye-split-sistemy?&limit_start={limit}'
    htmlPage = requests.get(linkToConditions).text
    soup = BeautifulSoup(htmlPage, 'html.parser')
    conditions = soup.find_all('div', {'class': 'block'})
    for condition in conditions:
        conditionName = condition.h2.text.strip()
        condiitionPrice = condition.find('span', {'class': 'price'}).span.text.strip()

        with open('conditions.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([conditionName, condiitionPrice])
            
        

    limit += limitStep
    if(soup.text.find('Товара с такими характеристиками не найдено, попробуйте изменить данные фильтра') != -1):
        print('Парсинг успешно завершен')
        break
    print(f'Спарсил {limit} товаров')

