import sys

#ARGOMENTI DA LINEA DI COMANDO
print(f'Argomenti da linea di comando: {sys.argv}')

print(f'Nome dello script: {sys.argv[0]}')

if len(sys.argv) > 1:
    print(f'Primo argomento: {sys.argv[1]}')
else:
    print(f'Nessun argomento fornito.')

#USCITA DAL PROGRAMMA
if len(sys.argv) < 2:
    print('Errore: nessun argomento fornito.')
    sys.exit(1) #USCITA CON CODICE DI ERRORE 1
print('PROGRAMMA ESEGUITO CORRETTAMENTE')

#INPUT E OUTPUT STANDARD
#LEGGERE INPUT UTENTE 
print('Inserisci nome: ')
g_nome = sys.stdin.readline().strip()

#SCRIVERE L"OUTPUT SU STDOUT
sys.stdout.write(f'Ciao, {g_nome}!\n')

#SCRIVERE MESSAGGI DI ERRORE
sys.stderr.write('Questo é un messaggio di errore!')

#VERIFICARE DIMENSIONE DI UN OGGETTO IN MEMORIA
g_list = [1,2,3,4,5]
print(f'Dimensione della lista: {sys.getsizeof(g_list)} byte')

#VERIFICARE SE UN MODULO É GIÁ IMPORTATO
if 'nome_modulo' in sys.modules:
    print('Modulo giá importato')
else:
    print('Modulo non importato')