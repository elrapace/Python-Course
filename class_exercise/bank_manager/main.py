#MAIN CLASS

#IMPORT CLASSES
from User import User
from BankManager import BankManager


#INZIALIZE USER
g_user1 = User(9889, 'Luca', 'Rossi', 'Male', '08-08-1993', 5700)
g_user2 = User(7654, 'Marzia', 'Gialli', 'Female', '12-05-1887', 2000)

#INZIALIZE BANK MANAGER && ADD USERS
g_bank_manager = BankManager()
g_bank_manager.add_users(g_user1, g_user2)
g_bank_manager.display()

#DEPOSIT
g_bank_manager.deposit(9889, 2000)
g_bank_manager.deposit(7654, 2000)
g_bank_manager.display_balance(9889)
g_bank_manager.display_balance(7654)

#TAKE AWAY
g_bank_manager.take_away(9889, 2000)
g_bank_manager.take_away(7654, 2000)
g_bank_manager.display_balance(9889)
g_bank_manager.display_balance(7654)