import re

#CAR TRAVEL COST CALCULATOR
def travel_cost_calculator(p_distance_km, p_consumo_lpkm, p_prezzo_litro):
    l_total_consumo = p_distance_km / p_consumo_lpkm
    l_total_cost = l_total_consumo * p_prezzo_litro
    return l_total_cost

print(f'TOTAL TRAVEL COST: {round(travel_cost_calculator(100, 19.6, 1.744), 2)} euro')


#TOTAL DAYS FOR PROJECT
def total_days_project(p_total_hours, p_hours_for_day):
    l_total_days = p_total_hours / p_hours_for_day 
    if isinstance(l_total_days, float):
        l_str_total = str(l_total_days)
        l_split_list = l_str_total.split('.')
        return (l_split_list[0], l_split_list[1])
    else:
        return l_total_days
    
g_total_days_result = total_days_project(20,8)
if type(g_total_days_result) is tuple:
    print(f'TOTAL DAYS FOR COMPLETE PROJECT: {g_total_days_result[0]} days and {g_total_days_result[1]} hours')
else:
    print(f'TOTAL DAYS FOR COMPLETE PROJECT: {g_total_days_result} days')


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

g_price_list = total_invoice_calculator([100,200,300], 22)
print(g_price_list)


#CONVERTER CELSIUS TO FAHRENHEIT
def converter_to_fahrenheit(p_celsius_list):
    return list(map(lambda l_item: (l_item * 9)/5 + 32, p_celsius_list))

g_celsius_values = [35, 78, 40]
g_fahrenheit_result = converter_to_fahrenheit(g_celsius_values)
print(f'CELSIUS VALUES: {g_celsius_values}')
print(f'FAHRENHEIT VALUES: {g_fahrenheit_result}')


#NUMBER OF WORDS IN PHRASE
def number_of_words(p_phrase):
    return len(p_phrase.split(' '))

def number_of_words_re(p_phrase):
    l_res_list = re.split('[\s,:;.!?]', p_phrase)
    print(f'SPLIT LIST(RE): {l_res_list}')
    l_filter_list = list(filter(lambda p_item: True if len(p_item) != 0 else False, l_res_list))
    print(f'FILTER LIST: {l_filter_list}')
    return len(l_filter_list)

g_phrase = "Hello World"
g_phrase1 = "Hello World. How are you?"
g_words_result = number_of_words(g_phrase)
print(f'PHRASE: {g_phrase}')
print(f'NUMBER OF WORDS: {g_words_result}')
g_words_result = number_of_words_re(g_phrase)
print(f'NUMBER OF WORDS WITH RE: {g_words_result}')
print(f'PHRASE: {g_phrase1}')
g_words_result = number_of_words_re(g_phrase1)
print(f'NUMBER OF WORDS WITH RE: {g_words_result}')