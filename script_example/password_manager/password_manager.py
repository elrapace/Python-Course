import json, time, sys
from tqdm import tqdm
from getpass_asterisk.getpass_asterisk import getpass_asterisk

g_dict_manager = {}

def insertAccount(p_name, p_username, p_password):
    #UPDATE DICT WITH NEW P_NAME, P_USERNAME, P_PASSWORD
    g_dict_manager[p_name] = {'username': p_username, 'password': p_password}
    return g_dict_manager

#DELETE ACCOUNT
def deleteAccount():
    takeJSON()
    l_account_name = ''
    while l_account_name == '':
        l_account_name = input('INSERT ACCOUNT NAME TO DELETE: ').title()

        if l_account_name in g_dict_manager:
            confirm = input(f'ARE YOU SURE YOU WANT TO DELETE ACCOUNT "{l_account_name}"? (y/n): ')
            if confirm.lower() == 'y':
                del g_dict_manager[l_account_name]
                # Update JSON after deletion
                with open('password_manager.json', 'w') as outfile:
                    json.dump(g_dict_manager, outfile, indent=4)
                print(f'ACCOUNT "{l_account_name}" DELETED SUCCESSFULLY!')
                return True
            else:
                print('DELETION CANCELLED.')
                return False
        else:
            print(f'ACCOUNT "{l_account_name}" NOT FOUND.')
            return False

#FUNCTION TO TAKE JSON FILE
def takeJSON():
    #TAKE JSON FILE
    global g_dict_manager
    try:
        with open('password_manager.json', 'r') as file:
            g_dict_manager = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        g_dict_manager = {}

#FUNCTION FOR WRITE AND SAVE NEW JSON FILE
def writeJSON(p_dict):
    with open('password_manager.json', 'w') as outfile:
	    json.dump(p_dict, outfile, indent=4)

def insertNewAccount():

    takeJSON()

    #INSERT NEW VALUE
    l_account_list = insertInput()

    #UPDATE DICT MANAGER
    l_update_dict = insertAccount(l_account_list[0], l_account_list[1], l_account_list[2])

    #WRITE AND SAVE NEW JSON FILE
    writeJSON(l_update_dict)

def insertInput():
    l_account_name = ''
    l_username = ''
    l_password = ''

    while l_account_name == '':
        l_account_name = input('INSERT ACCOUNT NAME: ')
        l_account_name = l_account_name.title()
        if l_account_name in g_dict_manager:
            print('ERROR! NAME ALREADY USED')
            l_account_name = ''
    
    while l_username == '':
        l_username = input(f'INSERT USERNAME FOR {l_account_name}: ')

    while l_password == '':
        l_password = input(f'INSERT PASSWORD FOR {l_account_name}: ')
        if isPasswordUsed(l_password):
            print('ERROR! PASSWORD ALREADY USED')
            l_password = ''
    return [l_account_name, l_username, l_password]

def isPasswordUsed(p_password):
    for l_account in g_dict_manager.values():
        if l_account['password'] == p_password:
            return True
    return False

#MODIFY ACCOUNT
def modifyAccount():
    l_account_name = ''
    while l_account_name == '':
        l_account_name = input('INSERT ACCOUNT NAME TO EDIT: ')
        takeJSON()
        l_account_name = l_account_name.title()

        for l_key, l_value in g_dict_manager.items():
            if l_key == l_account_name:
                print('WHAT WOULD YOU LIKE TO MODIFY?')
                print('1 - USERNAME')
                print('2 - PASSWORD')
                print('3 - BOTH')
                l_choice = input('ENTER CHOICE (1,2,3): ')

                
                l_username = l_value['username']
                l_password = l_value['password']

                if l_choice == '1' or l_choice == '3':
                    new_username = ''
                    while new_username == '':
                        new_username = input(f'INSERT NEW USERNAME FOR {l_account_name}: ')
                    l_value['username'] = new_username
                    l_username = new_username

                if l_choice == '2' or l_choice == '3':
                    new_password = ''
                    while new_password == '':
                        new_password = input(f'INSERT NEW PASSWORD FOR {l_account_name}: ')
                        if isPasswordUsed(new_password):
                            print('ERROR! PASSWORD ALREADY USED')
                            new_password = ''
                    l_value['password'] = new_password
                    l_password = new_password

                #SAVE NEW JSON FILE
                writeJSON(g_dict_manager)

                return [l_account_name, l_username, l_password]
            else:
                return []
        
#SEARCH ACCOUNT (PASSWORD & USERNAME)
def searchAccount(p_name):

    takeJSON()
    
    p_name = p_name.title()

    for l_key, l_value in g_dict_manager.items():
        if l_key == p_name:
            return [l_value['username'], l_value['password']]
    return []

#VIEW ALL ACCOUNTS
def viewAllAccounts():
    takeJSON()

    print("----- ALL ACCOUNTS -----")
    for l_key, l_value in g_dict_manager.items():
        print(f"ACCOUNT: {l_key}\nUSERNAME: {l_value['username']}\nPASSWORD: {l_value['password']}")
        print('------------------------')

#PRINT HELP COMMAND
def helpCommand():
    print('----- COMMANDS -----')
    print('1 - INSERT NEW ACCOUNT')
    print('2 - DELETE ACCOUNT')
    print('3 - SEARCH ACCOUNT')
    print('4 - VIEW ALL ACCOUNT')
    print('5 - EDIT ACCOUNT')
    print('6 - HELP COMMAND')
    print('7 - EXIT PROGRAM')
    print('--------------------')

def tqdmBar():
    for l_i in tqdm(range(100)):
        time.sleep(0.01)

#FUNCTION FOR EXIT PROGRAM
def exitProgram():
    print('CLOSING PROGRAM...')
    tqdmBar()
    print('CLOSED')
    sys.exit(1)

#FUNCTION FOR CHECK MASTER PASSWORD
def checkMasterPassword():

    l_master_password = ''

    #TAKE JSON FILE WITH MASTER PASSWORD
    try:
        with open('master.json', 'r') as file:
            l_master_password = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        l_master_password =  ''

    l_master_password = l_master_password["master"]

    print("----- LOGIN PASSWORD MANAGER -----")

    l_attempts = 3
    while l_attempts > 0:
        try:
            l_insert_password = getpass_asterisk("INSERT MASTER PASSWORD TO UNLOCK PROGRAM: ").strip()
        except KeyboardInterrupt:
            print('\nCTRL+C DETECTED!')
            exitProgram()

        if not l_insert_password:
            print("PASSWORD CANNOT BE EMPTY")
            continue
        if l_insert_password == l_master_password:
            print("ACCESS GRANTED!\n")
            return True
        else:
            l_attempts -= 1
            print(f"WRONG PASSWORD. ATTEMPTS LEFT: {l_attempts}")
    print("ACCESS DENIED.")
    exitProgram()