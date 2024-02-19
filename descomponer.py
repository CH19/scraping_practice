def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            # print("No es primo", n, "es divisor")
            return False
    # print("Es primo")
    return True
def descomponer(num: int):
    actual_num = num
    descomposition = []
    primos = []
    for i in range(2, num):
        if(es_primo(i)):
            primos.append(i)
    while actual_num > 1:
        for i in range(len(primos)):
            if(actual_num % primos[i] == 0): 
                actual_num /= primos[i]
                descomposition.append({"division": int(actual_num), "divisor": primos[i]})   
                break 
        print(actual_num)

    print(descomposition)
descomponer(16)