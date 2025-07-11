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

#MULTIPLE PRINT
def multiple_print():
    l_range_number = int(input('Inserisci un numero: '))
    for l_i in range(l_range_number):
        print('Hello Python!')

#COUNTER UPPERCASE AND LOWERCASE
def counter_case(p_string):
    l_count_u = 0
    l_count_l = 0
    l_count_other = 0
    l_len_str = len(p_string)
    for l_item in p_string[0:l_len_str]:
        if l_item.isalpha():
            if l_item.isupper():
                l_count_u += 1
            else:
                l_count_l += 1
        else:
            if l_item != ' ':
                l_count_other += 1
    return (l_count_l, l_count_u, l_count_other)


#FUNCTION LONGEST WORD
def longest_wordl(*p_str):
    l_obj_result = {}
    for l_str in p_str:
        l_obj_result[len(l_str)] = l_str
    l_max_key = max(l_obj_result)
    l_min_key = min(l_obj_result)
    l_list_return = []
    for l_key, l_values in l_obj_result.items():
        if l_key == l_max_key or l_key == l_min_key:
            l_list_return.append(l_values)
    return l_list_return
        

#FUNCTION CHECK ELEMENT
def check_element(p_list, p_element):
    if p_element in p_list:
        print('ELEMENT ALREADY PRESENT!')
    else:
        p_list.append(p_element)
        print(f'ELEMENT NOT PRESENT. INSERT ELEMENT: {p_element}')
    return p_list


#FUNCTION REMOVE DUPLICATE AND SORT
def remove_d_s(p_list):
    #REMOVE DUPLICATE
    l_result_list = list(dict.fromkeys(p_list))
    #SORT LIST
    l_result_list.sort()
    return l_result_list

#FUNCTION SECOND OCCURENCE
def second_occurrence(p_list, p_element):
    l_index_list = []
    for l_index, l_item in enumerate(p_list):
        if l_item == p_element:
            l_index_list.append(l_index)
    if len(l_index_list) < 2:
        return -1
    else:
        return  l_index_list[1]