def suma(*args):
    total = 0
    for i in args:
        total += i
    return total

compus = [1,3,4,5,1,3,2]
print(suma(3,2,5))
def printes_users(**user):
    data = list(user.items())
    mensaje = "Bienvenido " + data[0][1]
    if(data[1][1] == "Admin"):
        mensaje += " Admin"
    print(mensaje)

printes_users(name="Christian", rol="Admin")