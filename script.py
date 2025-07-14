import sys, os

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
print('--> ADD, OK!')

#ESEGUO IL COMMIT
os.system('git commit -m "Update"')
print('--> COMMIT, OK!')

#GIT PUSH
os.system('git push')
print('--> PUSH, OK!')