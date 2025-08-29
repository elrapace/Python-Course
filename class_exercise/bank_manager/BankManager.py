#CLASS BANK MANAGER
class BankManager:
    def __init__(self):
        self.repo = {}

    #ADD USER METHOD
    def add_users(self, *p_users):
        for l_user in p_users:
            self.repo[l_user.id] = l_user
            print(f'Add {l_user.id}!')
        print('\n')
        return True

    #REMOVE USER METHOD
    def remove_users(self, *p_users_id):
        for l_user_id in p_users_id:
            self.repo.pop(l_user_id)
            print(f'Remove {l_user_id}')
        print('\n')
        return True

    #TAKE AWAY METHOD
    def take_away(self, p_user_id, p_amount):
        if p_amount > 5:
            for l_user_id, l_user in self.repo.items():
                if l_user_id == p_user_id and l_user.balance > 0:
                    l_user.balance -= p_amount
                    print(f'New balance: {l_user.balance}\n')
                    return True
            print(f'Insufficient balance o user not found!\n')
            return False
        else:
            print(f"Amount very low!\n")
            return False

    #DEPOSIT METHOD
    def deposit(self, p_user_id, p_amount):
        if p_amount > 0:
            for l_user_id, l_user in self.repo.items():
                if l_user_id == p_user_id:
                    l_user.balance += p_amount
                    print(f'New balance: {l_user.balance}\n')
                    return True
            print(f'User not found!\n')
            return False
        else:
            print(f'Not deposit 0!\n')
            return False

    #DISPLAY BALANCE
    def display_balance(self, p_user_id):
        for l_user_id, l_user in self.repo.items():
            if l_user_id == p_user_id:
                print(f'Courrent balance is: {l_user.balance}\n')
                return True
        return False
            
    #DISPLAY ALL USERS
    def display(self):
        print('Users: ')
        for l_user_id, l_user in self.repo.items():
            print(f'ID: {l_user_id}, NAME: {l_user.name}, SURNAME: {l_user.surname}, SEX: {l_user.sex}, BIRTHDAY: {l_user.birthday}, BALANCE: {l_user.balance}')
        print('\n')