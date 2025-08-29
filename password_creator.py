#Function to generate a new account password
import random
import os
import time

def add_carac(p_str1, p_str2, p_len):
    l_random_index = random.randint(0, p_len - 1)
    return p_str2 + p_str1[l_random_index]

def generate_password():
    """Function to generate a new password (12 len) with 1 maiusc, 1 min, 1 number, 1 caract

    Returns:
        string: return new password string
    """
    l_string_min = 'abcdefghijklmnopqrstuvwxyz'
    l_string_ma = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l_string_number = '0123456789'
    l_string_c = '!@#$%*()_-/?<>'
    l_new_password = ''
    for l_i in range(3):
        l_new_password = add_carac(l_string_min, l_new_password, len(l_string_min))
        l_new_password = add_carac(l_string_ma, l_new_password, len(l_string_ma))
        l_new_password = add_carac(l_string_number, l_new_password, len(l_string_number))
        l_new_password = add_carac(l_string_c, l_new_password, len(l_string_c))
    return l_new_password

l_generated_password = generate_password()
# print('New password generated: ' + l_generated_password)

print('Saving new password in file.....')
password_file = open('generate_password_file.txt', 'w')
password_file.write('New password generated: ' + l_generated_password)
password_file.close()
print('Save completed')
g_file_stat = os.stat('generate_password_file.txt')
print(f'Dimension: {g_file_stat.st_size} byte')
g_local_time = time.ctime(g_file_stat.st_mtime)
print(f'Last modification: {g_local_time}\n')