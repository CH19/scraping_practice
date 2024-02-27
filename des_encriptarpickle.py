import pickle
def desenciptar(arch_name: str):
    archivo = open(arch_name, "rb")
    datos = pickle.load(archivo)
    archivo.close
    return datos
# print(desenciptar("data_nase.pkl"))
