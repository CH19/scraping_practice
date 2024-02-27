# # # Pickle es una formato de datos unico en python similar a json 
# # # con variaciones como que usea codigo binario para almacenarlo, podemos almaacenar cualquier cosa y a diferencia de json
# # # es menos seguro por el codigo binario al que se convierte 

import json
# # # para usarlo primero hay que importarlo es un modulo de la biblioteca standard
import pickle

# # # importamos el modulo json para trabajar con data 
# # # creamos un archivo con la extension pickle 
# # # archivo = open("data_nase.pkl", "wb")
arch_pickle = open("data_nase.pkl", "wb")

with open("users.json", "r") as archivo:
    new_data = json.loads(archivo.read())
pickle.dump(new_data, arch_pickle)
archivo.close()
arch_pickle.close()
