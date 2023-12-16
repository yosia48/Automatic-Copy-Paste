"""
Code By Yosia Ryan

Installation 
pip install pyautogui
pip install pyperclip

"""

import pyperclip
import time

def simpan_ke_file(teks):
    with open('copypaste.txt', 'a') as file:
        file.write(teks + '\n')

def cek_clipboard():
    teks_sebelum = ''
    while True:
        teks_saat_ini = pyperclip.paste()

        if teks_saat_ini != teks_sebelum:
            simpan_ke_file(teks_saat_ini)
            teks_sebelum = teks_saat_ini

        time.sleep(1)  # Menunda selama 1 detik

if __name__ == "__main__":
    cek_clipboard()
