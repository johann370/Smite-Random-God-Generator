import subprocess
import pandas as pd
from random import randint

def get_gods_list():
    data = pd.read_csv('gods.csv')
    return data

def get_random_god(god_list):
    max = len(god_list) - 1
    random_number = randint(0, max)
    random_god = god_list[random_number]
    return random_god

if __name__ == '__main__':
    #subprocess.call('god-scraper.py', shell=True)
    god_names = get_gods_list().God
    random_god = get_random_god(god_names)
    print(random_god)
