import requests
from bs4 import BeautifulSoup
import time

link = requests.get('https://www.imdb.com/title/tt8041270/?ref_=hm_tpks_tt_t_4_pd_tp1_cp')


url = link.text

soup = BeautifulSoup(url, 'lxml')


title = soup.title.text
print(title)

# title = soup.find('h1')
# print(title)


# tytuly = soup.find_all('h2')
# print(tytuly)

opis = soup.find('div','summary_text').text   # KOD Z TUTORIALU
print(opis)

opis = soup.find('div',attrs={'class':"sc-16ede01-0 fMPjMP"}).text  # MOJ KOD
print(opis)