#Semplice traduttore che legge da file e scrive la traduzione in un'altro file
from deep_translator import GoogleTranslator
try:
    with open('text1.txt', 'r') as file:
        l_file_text = file.read()
        l_translated = GoogleTranslator(source='auto', target='es').translate(l_file_text)
    with open('text2.txt', 'w') as file:
        file.write(l_translated)
except IOError:
    print('I/O error')