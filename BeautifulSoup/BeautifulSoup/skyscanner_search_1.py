from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# INSERIMENTO MESE DI PARTENZA & DI ARRIVO CON L'ANNO
g_anno_partenza = input('ANNO PARTENZA: ')
g_mese_partenza = input('MESE PARTENZA: ')

g_anno_ritorno = input('ANNO RITORNO: ')
g_mese_ritorno = input('MESE RITORNO: ')

# IMPOSTAZIONE PER LA MODALITÀ IN INCOGNITO
g_options = Options()
g_options.add_argument('-private')

# CREAZIONE ISTANZA DEL BROWSER FIREFOX
g_driver = webdriver.Firefox(options=g_options)

# VA ALLA PAGINA DESIDERATA
g_driver.get(f'https://www.skyscanner.it/trasporti/voli-da/psa/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=1&preferdirects=true&outboundaltsenabled=false&inboundaltsenabled=false&oym={g_anno_partenza}{g_mese_partenza}&iym={g_anno_ritorno}{g_mese_ritorno}')

# OTTENGO CODICE HTML DELLA PAGINA
g_html = g_driver.page_source

# CREAZIONE OGGETTO BS4
g_soup = BeautifulSoup(g_html, 'html.parser')

# # PRENDO IL DIV CHE CONTIENE TUTTE LE DESTINAZIONI
# g_div = g_soup.find('div', class_='ResultList_container__MjNkY')

# # PRENDO I LINK AL SUO INTERNO CHE SONO LE VARIE DESTINAZIONI
# g_links = g_div.find_all('a')

# for l_link in g_links:
#     # CERCO IL PRIMO SPAN DOVE DICE LA DESTINAZIONE E IL PREZZO
#     l_span = l_link.find('span')
#     l_string = l_span.string
#     l_st = l_string.split('a ')[1].split(',')
#     l_posto = l_st[0].strip()
#     l_price = l_string.split("€")[1].strip()
#     print(f'DESTINAZIONE: {l_posto}, PREZZO: € {l_price}')

# CHIUSURA DEL BROWSER
input('PREMI INVIO PER CHIUDERE IL BROWSER...')

g_driver.quit()