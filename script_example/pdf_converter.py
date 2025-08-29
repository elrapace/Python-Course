import sys, time, subprocess, os
from fpdf import FPDF

#FUNZIONE PER INSERIRE IL NOME DEL FILE PDF TRAMITE SHELL
def inputName():
    g_name = input('Insert name of pdf file: ')
    g_pdf_name = g_name + '.pdf'
    return g_pdf_name

g_pdf = FPDF()

if len(sys.argv) > 1:
    print(f'File name: {sys.argv[1]}')
else:
    print('No file! Insert file to convert')
    sys.exit(1)

g_pdf.add_page()

g_pdf.set_font("Arial", size = 15)

with open(sys.argv[1], 'r') as g_file:
    l_rows = g_file.readlines()
    for l_row in l_rows:
        g_pdf.cell(200, 10, txt=l_row, ln=1, align='S')
print('Converted!')

#INSERISCO IL NOME DEL FILE TRAMITE SHELL
g_name_result = inputName()

#CONTROLLO SE IL NOME DEL FILE PDF ESISTE GIÁ OPPURE NO    
while os.path.isfile(g_name_result):
    print('File name already used!')
    g_name_result = inputName()

g_pdf.output(g_name_result)

g_application = 'okular'
print(f'Opening file... : "{g_name_result}" with "{g_application}"')

time.sleep(1)

#APERTURA DEL FILE PDF TRAMITE 'OKULAR'
subprocess.run([g_application, g_name_result])