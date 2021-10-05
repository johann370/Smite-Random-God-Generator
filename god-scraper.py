from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import urllib.request
import requests


def get_gods():
    driver = webdriver.Chrome('C:/Users/dragonking370/Desktop/chromedriver_win32/chromedriver.exe')
    content = driver.get('https://smite.fandom.com/wiki/Smite_Wiki')
    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')
    gods = soup.find_all('div', style='display: inline-block;padding:1px;padding-right:5px')
    driver.close()
    godsList = []

    for god in gods:
        name = god.text
        a = god.select('span a')
        for el in a:
            link = f'https://smite.fandom.com{el["href"]}'
        godInfo = {
            'God': name,
            'Wiki': link
        }
        print(godInfo)
        godsList.append(godInfo)
    return godsList


def get_gods_updated():
    driver = webdriver.Chrome('C:/Users/dragonking370/Desktop/chromedriver_win32/chromedriver.exe')
    content = driver.get('https://smite.fandom.com/wiki/List_of_gods')
    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')
    gods = soup.find('tbody').find_all('tr')
    driver.close()
    gods_list = []

    for god in gods:
        god_data = god.find_all('td')
        name = god_data[1].text
        href = god_data[1].find('a').get('href')
        link = f'https://smite.fandom.com{href}'
        pantheon = god_data[2].text
        god_class = god_data[5].text
        release_date = god_data[9].text

        god_info = {
            'God': name,
            'Link': link,
            'Pantheon': pantheon,
            'Class': god_class,
            'Release_Date': release_date
        }
        gods_list.append(god_info)
    return gods_list


def download_god_image(link):
    content = requests.get(link).content
    soup = BeautifulSoup(content, 'lxml')
    god_info = soup.find('tbody').find_all('tr')

    name = god_info[0].text.strip()

    if(name == 'This page refers to content that has yet to be released and may contain inaccuracies. Nothing here is final and anything is subject to change.'):
        return

    image_link = god_info[1].find('a').get('href')
    urllib.request.urlretrieve(image_link, f'./images/{name}.jpg')
    print(f'Downloading {name}.jpg')


def export_gods_to_csv(gods):
    df = pd.DataFrame(gods)
    df.to_csv('gods.csv', index=False)


if __name__ == "__main__":
    gods = get_gods_updated()
    export_gods_to_csv(gods)
    links = list()

    for god in gods:
        links.append(god.get('Link'))

    for link in links:
        download_god_image(link)
