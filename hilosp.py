from datetime import datetime
import time
from standard import es_primo, limpiarPantalla
# usando hilos 
import threading


def mostrar_color(color: str):
    for i in range(10):
        hora = datetime.now().strftime("%H:%M:%S.%f")
        print(f"{color}#{i}: {hora} gris")
        time.sleep(0.01)
mostrar_color("Verde")

if __name__ == "__main__":
    inicio = datetime.now()
    h1 =    threading.Thread(name="Hilo1", target=mostrar_color, args=("Verde",))
    h2 = threading.Thread(name="Hilo Amarillo", target=mostrar_color, args=("Amarillo",))
    h3 = threading.Thread(name="es_primo",target=es_primo, args=(2670,))
    imprimir = threading.Thread(name="impresor", target=print, args=("Hola muchacho comoe sta",))

    print(f"{threading.main_thread().ident} {threading.main_thread()} ")
    limpiarPantalla()
    # inciamos los hilos 
    h1.start()
    h2.start()
    h3.start()
    imprimir.start()
    imprimir.join()
    h3.join()
    h2.join()
    h1.join()

    print(f"Finalizado en {datetime.now() - inicio}")