import random
import platform
import os

# Escribir un juego para adivinar una palabra con las palabras desordenadas 

def limpiarPantalla():
    so = platform.system()
    if so == "Windows":
        os.system("cls")
        return
    os.system("clear")

def game():
    def getRandomWord():
        word = input("Escribe una palabra")
        random_word = random.shuffle(list(word))
        return random_word
    print(getRandomWord())
game()  
