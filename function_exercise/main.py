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