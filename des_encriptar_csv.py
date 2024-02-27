import csv, json, pickle
from datetime import datetime
all_data = []
with open("BTCUSDT.csv", "r", encoding="utf8") as f:
    filas = csv.reader(f)
    for fila in filas: 
        fecha = datetime.fromtimestamp(int(fila[0])/1000)
        opcciones = ("open", "high", "low", "close", "volumen")
        data = {"fecha": fecha}
        for  op in opcciones:
            
            num = op
            cosa = opcciones[0]
            data.update({op: float(fila[opcciones.index(op) + 1]) })
        all_data.append(data) 
# new_data = "\n".join(str(diccionario ) for diccionario in all_data)
with open("usdt_data_base.json", "a") as archivo:
    for data in all_data:
        archivo.write(json.loads(str(data)))


