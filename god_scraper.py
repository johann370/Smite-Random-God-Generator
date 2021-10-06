import os
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import requests


def get_gods():
    content = requests.get('https://smite.fandom.com/wiki/List_of_gods').content
    soup = BeautifulSoup(content, 'lxml')
    gods = soup.find('tbody').find_all('tr')[1:]
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

    if (name == 'This page refers to content that has yet to be released and may contain inaccuracies. Nothing here '
                'is final and anything is subject to change.'):
        return

    image_link = god_info[1].find('a').get('href')
    urllib.request.urlretrieve(image_link, f'./images/{name}.jpg')
    print(f'Downloading {name}.jpg')


def export_gods_to_csv(gods):
    df = pd.DataFrame(gods)
    df.to_csv('gods.csv', index=False)


def main():
    os.mkdir('./images/')
    gods = get_gods()
    export_gods_to_csv(gods)
    links = list()

    for god in gods:
        links.append(god.get('Link'))

    for link in links:
        download_god_image(link)
