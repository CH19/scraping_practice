def get_demanda(p: float, ps: float, yd: float):
    return p - ps + yd
ingresos = [20,2,10,5,100,30,40,20,3,4,2,18]
promedio = 0
q_data = []
for i in ingresos:
    data = get_demanda(12,15, i)
    q_data.append(data)
    promedio += i
result = promedio / len(q_data)
print(f"El producto es demandando en {round(result, 2)} q")

