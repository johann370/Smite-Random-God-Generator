import GUI
import god_scraper


def update():
    update = input('Would you like to update the gods list/images? (Y/N): ')
    if update == 'Y':
        god_scraper.main()


def run_program():
    GUI.main()


if __name__ == '__main__':
    update()
    run_program()
