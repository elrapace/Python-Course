from password_manager import *

g_command = ''
checkMasterPassword()
helpCommand()

try:
    while g_command == '':
        g_command = input('->INSERT COMMAND: ')
        if g_command.isnumeric():
            #INSERT NEW ACCOUNT
            if g_command == '1':
                print('\n')
                insertNewAccount()
                g_command = ''

            #DELETE ACCOUNT
            elif g_command == '2':
                print('\n')
                success = deleteAccount()
                if not success:
                    print('ERROR! ACCOUNT NOT DELETED!')
                g_command = ''


            #SEARCH ACCOUNT
            elif g_command == '3':
                print('\n')
                l_name = input('INSERT NAME OF ACCOUNT: ')
                l_search_result = searchAccount(l_name)
                if l_search_result == []:
                    print('ERROR! NAME OF ACCOUNT NOT FOUND')
                else:
                    print('------------------------------')
                    print(f'ACCOUNT: {l_name}\nUSERNAME: {l_search_result[0]}\nPASSWORD: {l_search_result[1]}')
                    print('------------------------------')
                g_command = ''
            
            #VIEW ALL
            elif g_command == '4':
                print('\n')
                viewAllAccounts()
                g_command = ''

            #MODIFY ACCOUNT
            elif g_command == '5':
                print('\n')
                l_modify_result = modifyAccount()
                if l_modify_result == []:
                    print('ERROR DURING MODIFICATION...! NAME OF ACCOUNT NOT FOUND')
                else:
                    print('------------------------------')
                    print(f'ACCOUNT: {l_modify_result[0]}\nUSERNAME: {l_modify_result[1]}\nPASSWORD: {l_modify_result[2]}')
                    print('------------------------------')
                g_command = ''

            #HELP COMMANDS
            elif g_command == '6':
                print('\n')
                helpCommand()
                g_command = ''

            #EXIT PROGRAM
            elif g_command == '7':
                print('\n')
                exitProgram()

            else:
                print('COMMAND NOT FOUND!')
                helpCommand()
                g_command = ''
        else:
            g_command = ''
except KeyboardInterrupt:
    print('\nCTRL+C DETECTED!')
    exitProgram()
