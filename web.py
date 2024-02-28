# usando las primeras funciones para python en web 
from urllib.request import urlopen
import os
# Importamos la funcion urlopen que nos permitira abrir url con mucha facilidad 
# creamos un string con una url 


def clear_screen():
    if os.name == "Windows":
        os.system("cls")
        return
    os.system("clear")

# obtener todo el codigo html de una pagina 
def get_html(url: str):
    req = urlopen(url)
    html = req.read().decode("utf-8")    
    return html

# Obtener un archivo binario de una pagina web


def make_file_fromhtml():
    url = input("Escribe el link para obtener la data: ")
    formato = input("Escribe el nombre del archivo con la extension a descargar:  ")

    # hacemos el req para la peticion 
    newDocument = open(formato, "w", encoding="utf-8")
    newDocument.write(get_html(url=url))
    newDocument.close()
def get_file_from_link():
    url = input("Escribe el link para obtener la data: ")
    formato = input("Escribe el nombre del archivo con la extension a descargar:  ")

    # hacemos el req para la peticion 
    newDocument = open(formato, "wb")
    newDocument.write(getFile(url))
    newDocument.close()

while True:
    print("Bienvenido a nuestro programa para obtener data de links")
    print("1. Obtener contenido de una pagina")
    print("2. Obtener file de un link")

    print("3. salir")
    option = input("Key:")
    clear_screen()
    match(option):
        case "1":
            make_file_fromhtml()
        case "2":
            get_file_from_link()
        case "3":
            break
        
        case _: 
            print("opccion inexistente reintente nuevamente")
