import re
import matplotlib.pyplot as plt

def bestWordFile():
    try:
        with open('file.txt', 'r') as file:
            l_rows = file.readlines()
            l_result_dict = {}
            for l_row in l_rows:
                l_res_list = re.split('[\s,:;.!?]', l_row)
                l_filter_list = list(filter(lambda p_item: True if len(p_item) != 0 else False, l_res_list))
                for l_word in l_filter_list:
                    l_counter = l_filter_list.count(l_word)
                    l_result_dict[l_word] = l_counter
            # print(l_result_dict)
            l_max_k, l_max_v = max(l_result_dict.items(), key=lambda x: x[1])
            print(f'MOST COMMON WORD IS: "{l_max_k}" WITH "{l_max_v}"')
            return l_result_dict
    except FileNotFoundError:
        print('FILE NOT EXIST')

def dataExtraction(p_data):
    l_result_list = []
    l_key_list = []
    l_value_list = []
    for l_key, l_value in p_data.items():
        l_key_list.append(l_key)
        l_value_list.append(l_value)
    l_result_list.append(l_key_list)
    l_result_list.append(l_value_list)
    return l_key_list, l_value_list

g_result = bestWordFile()
g_key, g_value = dataExtraction(g_result)
plt.bar(g_key, g_value)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Most common word", fontdict = font1)
plt.xlabel("Words", fontdict = font2)
plt.ylabel("Occurrences", fontdict = font2)

plt.show()