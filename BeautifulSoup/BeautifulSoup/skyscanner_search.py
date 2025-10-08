from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# RICHIESTA DATA PARTENZA & DATA ARRIVO
g_data_partenza = input('INSERISCI DATA PARTENZA (SOLO NUMERO DEL GIORNO ES: 03): ')
g_data_arrivo = input('INSERISCI DATA ARRIVO (SOLO NUMERO DEL GIORNO ES: 15): ')

# IMPOSTAZIONE PER LA MODALITÀ IN INCOGNITO
g_options = Options()
g_options.add_argument('-private')

# CREAZIONE ISTANZA DEL BROWSER FIREFOX
g_driver = webdriver.Firefox(options=g_options)


# VA ALLA PAGINA DESIDERATA
g_driver.get(f'https://www.skyscanner.it/trasporti/voli/psa/ory/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=2512&iym=2512&selectedoday={g_data_partenza}&selectediday={g_data_arrivo}')

# OTTENGO CODICE HTML DELLA PAGINA
g_html = g_driver.page_source

# CREAZIONE OGGETTO BS4
g_soup = BeautifulSoup(g_html, 'html.parser')

g_div = g_soup.find('div', class_='month-view-variant-total-trip-cost__price')
g_span = g_div.find_all('span')[0]
print(f'PREZZO TOTALE DEL VOLO: {g_span.string}')

# CHIUSURA DEL BROWSER
input('PREMI INVIO PER CHIUDERE IL BROWSER...')

g_driver.quit()