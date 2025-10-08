from pynput import keyboard

# Funzione che viene chiamata quando un tasto viene premuto
def on_press(key):
    try:
        # Mostra il tasto premuto
        print(f'Tasto premuto: {key.char}\n')
    except AttributeError:
        # Gestisce i tasti speciali come F1, Shift, Ctrl, ecc.
        print(f'Tasto speciale premuto: {key}\n')

# Configura l'ascolto dei tasti
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()