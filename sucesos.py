# Practica de estadistica con python 
# El array muestra los datos de cuando el indice bursatil dow Jonse sube un dia o no 
s = [
    # Primer dia
    {1: True, 2: True}, 
    # Segundo dia
    {
    1: True,
    2: False
}, 
# Tercer diea
{
    1: False,
    2: True
},
# Cuarto dia
{
    1: False,
    2: False
}
]
# Hay que evaluar los indices en el que sube un dia 
# primero se evalua los indices que sube el dia uno 
sube_el_primer_dia = list(filter(lambda x: x[1] == True, s))
sube_el_segundo_dia = list(filter(lambda x: x[2] == True, s))
print(sube_el_primer_dia)
print(sube_el_segundo_dia)

es_true = []

for i in s:
    pass