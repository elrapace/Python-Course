import sys, os, datetime

#CONTROLLO IL SECONDO AROGMENTO DOPO IL NOME DELLO SCRIPT, PRENDO IL PERCORSO IN CUI ESEGUIRE LO SCRIPT
if len(sys.argv) < 2:
	print(f'--> ERROR ❌, NO ARGUMENTS! SYNTAX: <python3 {sys.argv[0]} /path>')
	sys.exit(1) #USCITA CON CODICE DI ERRORE 1
	
print('--> SCRIPT START...')

#CAMBIO DIRECTORY DI LAVORO
os.chdir(sys.argv[1])
print(f'--> CURRENT DIRECTORY: {os.getcwd()}')

#ESEGUO COMANDI GIT
g_exit_code = os.system('git add --all')

if g_exit_code == 0:
    print('--> ADD, DONE ✅')
else:
     print('--> ERROR ADD ❌')

#ESEGUO IL COMMIT
g_data_commit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
g_commit_msg = f'Update {g_data_commit}'
g_exit_code = os.system(f'git commit -m "{g_commit_msg}"')

if g_exit_code == 0:
    print('--> COMMIT, DONE ✅')
else:
    print('--> ERROR COMMIT ❌')

#ESEGUO IL PUSH
g_exit_code = os.system("git push")

if g_exit_code == 0:
    print('--> PUSH, DONE ✅')
else:
    print('--> ERROR PUSH ❌')
