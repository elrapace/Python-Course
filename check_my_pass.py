import requests
import hashlib
import sys
import getpass

#Faccio la richiesta usando solo i primi 5 caratteri hash della password, e come risposta ottengo tute le hash di password che iniziano cosí
def requests_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again!')
    return res

#Restituisce il numero di volte in cui la password é stata violata
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    #Check password if it exists in API response
    #Transalate password in hash password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    #Chiama l'api con 5 caratteri
    response = requests_api_data(first5_char)
    #cerco il tail nella response, per vedere se é stata violata (cioé cerco se la parte restante della password da 6 char in poi é in una delle password delle risposte)
    return get_password_leaks_count(response, tail)

def main():
    try:
        password = getpass.getpass('🔐 Inserisci la tua password da verificare: ')
        if not password:
            print("⚠️ La password non può essere vuota!")
            return
        count = pwned_api_check(password)
        if count:
            print(f'❌ La password è stata trovata {count} volte. Cambiala subito!')
        else:
            print('✅ Nessuna traccia della tua password. Sembra sicura (per ora)!')
    except Exception as e:
        print(f'Errore: {e}')

if __name__ == '__main__':
    main()