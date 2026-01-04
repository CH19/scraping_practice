from urllib.request import urlopen
import csv, json

# hacemos la peticion a la api de binance para obtener datos de las monedas con las que queremos trabajar

req = urlopen("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m")
# convertimos los datos solicitados a formato json usando el metodo json.loads 
datos = json.loads(req.read())

# creamos el archivo csv para almacenar los datos y anadimos el modo de escritora con 
# enconding de utf8 para hacerlo en lenguaje natural
with open("USDTVES.csv", mode="w", encoding="utf8") as f:
    # usamos el metodo writer del objeto csv para escribir el archivo 
    writer = csv.writer(f, lineterminator="\n")
    for fila in datos:
        print(fila)
        # mencionamos cuando termina la fila 
        writer.writerow(fila)
