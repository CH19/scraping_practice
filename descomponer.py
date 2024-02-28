from standard import descomponer
import os

def clear_screen():
    os.system("cls")    



num = input("Ingresa el numero que deseas descomponer: ")
clear_screen()
descomponer(int(num))