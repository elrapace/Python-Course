import webbrowser


# APERTURA DELLA PAGINA
# webbrowser.open('https://www.geeksforgeeks.org/python/python-launch-a-web-browser-using-webbrowser-module/')

# APERTURA PAGINA IN UNA NUOVA FINESTRA DEL BROWSER
# webbrowser.open_new('https://www.geeksforgeeks.org/python/python-launch-a-web-browser-using-webbrowser-module/')

# APERTURA PAGINA IN UNA NUOVA SCHEDA DEL BROWSER
# webbrowser.open_new_tab('https://www.geeksforgeeks.org/python/python-launch-a-web-browser-using-webbrowser-module/')

# APERTURA SPECIFICANDO IL BROWSER 
g_browser = webbrowser.get('firefox')
g_browser.open_new('https://www.geeksforgeeks.org/python/python-launch-a-web-browser-using-webbrowser-module/')