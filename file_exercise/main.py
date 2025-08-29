g_file_name = 'file.txt'

#ES 1
# try:
#     with open(g_file_name, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print('ERROR, FILE NOT FOUND!')

#ES 2
# with open(g_file_name, 'r') as file:
#     l_lines = file.readlines()
#     for l_line in l_lines:
#         print(l_line.strip())

#ES 3
# with open(g_file_name, 'r') as file:
#     for l_item in range(5):
#         l_line = file.readline()
#         print(l_line.strip())

#ES 4
import re
def words_number(p_file_name):
    try:
        with open(p_file_name, 'r') as file:
            l_lines = file.readlines()
            for l_line in l_lines:
                l_res_list = re.split('[\s,:;.!?]', l_line)
                l_filter_list = list(filter(lambda p_item: True if len(p_item) != 0 else False, l_res_list))
            return len(l_filter_list) * len(l_lines)
    except FileNotFoundError:
        print('ERRORE, FILE NON ESISTENTE!')

g_result = words_number(g_file_name)
print(f'NUMBER OF WORDS IN FILE: {g_result}')