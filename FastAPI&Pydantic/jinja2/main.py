from jinja2 import Environment, FileSystemLoader

# CARICAMENTO TEMPLATES DALLA CARTELLA 'TEMPLATES'
env = Environment(loader=FileSystemLoader('templates'))

# CARICHIAMO IL SINGOLO TEMPLATE SUL QUALE LAVORIAMO
template = env.get('hello.html')

#  DATI DA PASSARE AL TEMPLATE
data = {
    'name' : 'Alice',
    'age' : '23'
}

# RENDER DEL TEMPLATE CON I DATI
html_output = template.render(data)