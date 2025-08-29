from utility import *

#FUNCTION 1
print(f'TOTAL TRAVEL COST: {round(travel_cost_calculator(100, 19.6, 1.744), 2)} euro')

#FUNCTION 2
g_total_days_result = total_days_project(20,8)
if type(g_total_days_result) is tuple:
    print(f'TOTAL DAYS FOR COMPLETE PROJECT: {g_total_days_result[0]} days and {g_total_days_result[1]} hours')
else:
    print(f'TOTAL DAYS FOR COMPLETE PROJECT: {g_total_days_result} days')

#FUNCTION 3
g_price_list = total_invoice_calculator([100,200,300], 22)
print(g_price_list)

#FUNCTION 4
g_celsius_values = [35, 78, 40]
g_fahrenheit_result = converter_to_fahrenheit(g_celsius_values)
print(f'CELSIUS VALUES: {g_celsius_values}')
print(f'FAHRENHEIT VALUES: {g_fahrenheit_result}')

#FUNCTION 5
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

#FUNCTION 6
#multiple_print()

#FUNCTION 7
g_string = 'HELLO python!'
g_count_result = counter_case(g_string)
print(f'STRING: {g_string}')
print(f'NUMBER LOWERCASE: {g_count_result[0]}, NUMBER UPPERCASE: {g_count_result[1]}, OTHER: {g_count_result[2]}')

#FUNCTION 8
g_str1 = 'Hello python!'
g_str2 = 'a'
g_str3 = 'abc'
l_longest_result = longest_wordl(g_str1, g_str2, g_str3)
print(f'MAX AND MIN STRING ARE: {l_longest_result}')


#FUNCTION 9
l_list = ['30', '3', '5', '20']
l_element = '4'
print(f'ELEMENT: {l_element}')
print(f'CHECK ELEMENT LIST: {check_element(l_list, l_element)}')


#FUNCTION 10
l_list = ['Bmw', 'Mercedes', 'Audi', 'Ford', 'Mercedes']
print(f'RESULT AFTER REMOVE AND SORT: {remove_d_s(l_list)}')

#FUNCTION 11
l_element = 'Mercedes'
l_second_result = second_occurrence(l_list, l_element)
if l_second_result == -1:
    print(f'THERE ARE NOT 2 OCCURRENCE OF {l_element}')
else:
    print(f'INDEX OF SECOND OCCURRENCE OF {l_element} IS: {l_second_result}')