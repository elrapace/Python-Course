import re

#CAR TRAVEL COST CALCULATOR
def travel_cost_calculator(p_distance_km, p_consumo_lpkm, p_prezzo_litro):
    l_total_consumo = p_distance_km / p_consumo_lpkm
    l_total_cost = l_total_consumo * p_prezzo_litro
    return l_total_cost

#TOTAL DAYS FOR PROJECT
def total_days_project(p_total_hours, p_hours_for_day):
    l_total_days = p_total_hours / p_hours_for_day 
    if isinstance(l_total_days, float):
        l_str_total = str(l_total_days)
        l_split_list = l_str_total.split('.')
        return (l_split_list[0], l_split_list[1])
    else:
        return l_total_days

#CALCULATE TOTALE INVOICE
def total_invoice_calculator(p_price_list, p_iva_percent):
    l_result = []
    for l_price in p_price_list:
        l_total = new_price_iva(l_price, p_iva_percent)
        l_item = {
            'initial price':l_price,
            'iva':p_iva_percent,
            'new_price' : l_total
        }
        l_result.append(l_item)
    return l_result
#CALCULATE NEW PRICE WITH IVA
def new_price_iva(p_price, p_iva):
    l_iva = p_price * (p_iva / 100)
    l_total = p_price + l_iva
    return round(l_total, 2)

#CONVERTER CELSIUS TO FAHRENHEIT
def converter_to_fahrenheit(p_celsius_list):
    return list(map(lambda l_item: (l_item * 9)/5 + 32, p_celsius_list))

#NUMBER OF WORDS IN PHRASE
def number_of_words(p_phrase):
    return len(p_phrase.split(' '))

def number_of_words_re(p_phrase):
    l_res_list = re.split('[\s,:;.!?]', p_phrase)
    print(f'SPLIT LIST(RE): {l_res_list}')
    l_filter_list = list(filter(lambda p_item: True if len(p_item) != 0 else False, l_res_list))
    print(f'FILTER LIST: {l_filter_list}')
    return len(l_filter_list)