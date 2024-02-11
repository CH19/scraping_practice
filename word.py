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
    def getRandomWord(word: str):
        random_word = word.split()
        random.shuffle(random_word)
        return " ".join(random_word)
    def tryWord(word1: str):
        limpiarPantalla()
        intentos = 0
        random_word = getRandomWord(word)
        mensajes_fallo = ["Error sigue intentando", "Sabemos que eres mejor prueba otro", "Oracion incorrecta prueba con otra", "Organiza mejor las oraciones"]
        while True:
            if(intentos > 0):
                print(f"intentos: {intentos}")
                print("si te rindes presiona 5")
            print(f"la oracion es: {random_word}")
            word_comparing = input("Organiza la oracion:")
            if word_comparing == word1.lower():
                limpiarPantalla()
                print("La oracion esta organizada felicidades")    
                print(f"lo hiciste en el intento {intentos}")
                break
            elif word_comparing == 5:
                print("Asi que eres un cobarde esperemos que lo logres la proxima vez")
                break
            else:
                limpiarPantalla()
                print(f"{random.choice(mensajes_fallo)}")
                intentos+= 1
    limpiarPantalla()
    word = input("Escribe una palabra: ")
    tryWord(word)
    print("Gracias por jugar")
game()  
