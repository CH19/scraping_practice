# expresiones regulares python 
import re
text = "La lluvia de sevilla estuvo la cama presnete aqui caña"
x =re.search(r"c..a", text)
print(x)
print(dir(x))