import sys, os, datetime

#CONTROLLO IL SECONDO AROGMENTO DOPO IL NOME DELLO SCRIPT CHE PRENDO IL PERCORSO IN CUI ESEGUIRE LO SCRIPT
if len(sys.argv) < 2:
	print('--> ERROR, NO ARGUMENTS!')
	sys.exit(1) #USCITA CON CODICE DI ERRORE 1
	
print('--> SCRIPT RUN')

#CAMBIO DIRECTORY DI LAVORO
os.chdir(sys.argv[1])
print(f'--> CURRENT DIRECTORY: {os.getcwd()}')

#ESEGUO COMANDI GIT
os.system('git add --all')
print('--> ADD, DONE!')

#ESEGUO IL COMMIT
g_data_commit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
g_commit_msg = f'Update {g_data_commit}'
os.system(f'git commit -m "{g_commit_msg}"')
print('--> COMMIT, DONE!')

#GIT PUSH
os.system('git push')
print('--> PUSH, DONE!')