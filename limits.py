def lim(n: int ): 
    denominador = (n - 2)
    if denominador == 0: 
        return "Opearacion invalida denominador en 0"
    
    opearation = (2 *( n ** 2) - 4 * n) / denominador

    if opearation == 0:
        return "Limite inexistente"
    return "El limite es:" + str(opearation)


range_max = 10
range_min = 0
range_max -= .1 
print(range_max)

while range_max > 0 :
    range_max -= 1
    range_min += .1
    print(str(range_min) + "==" + str(range_max))
