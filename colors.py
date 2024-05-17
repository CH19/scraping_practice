from datetime import datetime
import time
import random

def generar_colors(color_arr: list):
    for i in range(32, 39):
        random_num =  "1" if random.random() > .4 else "0"
        color_arr.append(f"\33[{random_num};{i}]")
        time.sleep(0.1)

def mostrar_hora(color_arr):
    for n in range(20):
        color = color_arr[0]
        hora = datetime.now().strftime("%H:%M:%S.%f")
        print(f"{color}#{n}: {hora}{color}")
        time.sleep(0.01)
    pass

#colores
colors = []
generar_colors(color_arr=colors)
mostrar_hora(color_arr=colors)
print(colors[3])
