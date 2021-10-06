import subprocess


def update():
    update = input('Would you like to update the gods list/images? (Y/N): ')
    if update == 'Y':
        subprocess.call('god_scraper.py', shell=True)


def run_program():
    subprocess.call('GUI.py', shell=True)


if __name__ == '__main__':
    update()
    run_program()
