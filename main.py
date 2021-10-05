import subprocess
import pandas as pd
from random import randint
from God import God


def get_gods_list():
    data = pd.read_csv('gods.csv')
    return data


def create_god_objects(god_list):
    god_objects = list()
    for i in range(len(god_list)):
        name = god_list.God[i]
        link = god_list.Link[i]
        pantheon = god_list.Pantheon[i]
        god_class = god_list.Class[i]
        release_date = god_list.Release_Date[i]
        god = God(name, link, pantheon, god_class, release_date)
        god_objects.append(god)
    return god_objects


def get_random_god(god_list):
    max = len(god_list) - 1
    random_number = randint(0, max)
    random_god = god_list[random_number]
    return random_god


def get_god_image(god):
    return f'./images/{god.get_name()}.jpg'



def main():
    # subprocess.call('god-scraper.py', shell=True)
    god_list = create_god_objects(get_gods_list())

    random_god = get_random_god(god_list)
    return random_god


if __name__ == '__main__':
    main()
