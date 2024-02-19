from tabulate import tabulate
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
num = input("Ingresa el numero que deseas descomponer: ")

descomponer(int(num))