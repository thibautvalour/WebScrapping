import time
from genbrowser import Entry
import navigation



def scrapp(email, password):

    # Acces and log in Kartable
    entry = Entry(email, password)
    entry.start()
    entry.logger.info('Connexion')
    time.sleep(2)

    # Navigation
    navigation.level_step(entry)

if __name__ == '__main__':
    scrapp(email='thibautvalour3008@gmail.com', password='Rugbycase42')
