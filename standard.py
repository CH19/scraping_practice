import os, platform
from tabulate import tabulate
from urllib.request import urlopen

# permite ver la informacion de un archivo html 
def getFile(url: str):
    req = urlopen(url)
    file = req.read()
    return file
# limpia la pantalla 
def limpiarPantalla():
    so = platform.system()
    if so == "Windows":
        os.system("cls")
        return
    os.system("clear")

# hace un recocrrido si el numero seleccionado es primo o no 
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            # print("No es primo", n, "es divisor")
            return False
    # print("Es primo")
    return True

# Descompone un numero con todos sus divisores 
def descomponer(num: int):
    actual_num = num
    descomposition = []
    primos = []
    for i in range(2, (num + 1)):
        if(es_primo(i)):
            primos.append(i)
    try:
       if( primos.index(num)):
           print("Es un numero primo")
           return
    except ValueError:
        pass
    while actual_num > 1:
        for i in range(len(primos)):
            if(actual_num % primos[i] == 0): 
                actual_num /= primos[i]
                descomposition.append([int(actual_num),primos[i]])   
                break
    print("Numero", num)
    print(tabulate(descomposition, headers=["Division", "Divisor"], tablefmt="grid"))