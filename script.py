import os
import platform
import random
def limpiarPantalla():
    so = platform.system()
    if so == "Windows":
        os.system("cls")
        return
    os.system("clear")
# nnlimpiarPantalla()

def invocarRandoms():
    for i in range(1, 10):
    # crea dos numeros random de tipo float
        print(random.uniform(1,10))
    # crea un numero random entero 
        print(random.randint(2, 10))

# elegir un elemento random de una lista o elemento iterable
def elegirDataList(lista = ["Juan", "Ppedr", "miguel", "stuart", "Miguel", "andres", "JEsus"]):
    # con esta funcion llamamos un metodo random en una lista 
    print(lista)
    print(random.choice(lista))
def usandoSplit(str: str):
    lista_strings = str.split(" ")
    print(lista_strings)
    return lista_strings
def joinNames(list: list = ["Juan", "Ppedr", "miguel", "stuart", "Miguel", "andres", "JEsus"]):
    # Probando el metodo join en python 
    return "_".join(list)
print(joinNames())

