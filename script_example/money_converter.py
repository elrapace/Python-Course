from currency_converter import CurrencyConverter
from datetime import date
from tqdm import tqdm
import sys, os, time

c = CurrencyConverter()
g_conversion_value = ['EUR', 'USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']

#FUNCTION FOR CONVERSION
def converter():
    g_amount = float(input('ENTER AMOUNT: '))
    while g_amount < 0:
        print('ERROR, INSERT POSITIVE AMOUNT')
        g_amount = float(input('ENTER AMOUNT: '))
    
    g_currency = input('FROM: ').upper()
    while g_currency not in g_conversion_value:
        print('ERROR, INSERT VALID VALUE: ')
        print(f'{g_conversion_value}')
        g_currency = input('FROM: ').upper()
    
    g_new_currency = input('TO: ').upper()
    while g_new_currency not in g_conversion_value:
        print('ERROR, INSERT VALID VALUE: ')
        print(f'{g_conversion_value}')
        g_new_currency = input('TO: ').upper()

    g_amount = round(g_amount, 2)

    g_result = c.convert(g_amount, g_currency, g_new_currency, date=date(2024, 11, 5))
    g_rounded = round(g_result, 2)

    print(f'{g_amount} {g_currency} = {g_rounded} {g_new_currency}')

#FUNCTION TO PRINT HELP MENU
def helper():
    print('CONVERSION VALUE ARE: ')
    print(f'{g_conversion_value}')

def tqdmBar():
    for l_i in tqdm(range(100)):
        time.sleep(0.01)

g_command = input('->INSERT COMMAND: ')
while g_command.lower() != 'exit':
    if g_command.lower() == 'converter':
        converter()
    elif g_command.lower() == 'help':
        helper()
    else:
        print('INSERT VALID COMMAND')
    g_command = input('->INSERT COMMAND: ')

print('SHELL CLEANING AND CLOSING...')
tqdmBar()
os.system('clear')
sys.exit(1)