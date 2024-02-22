class Animal:
    especie = ""
    def __init__(self, especie) -> None:
        self.especie = especie
    def hablar(self, sonido = especie):
        sound = sonido
        especies = ["dog", "vaca", "cat", "horse"]
        for esp in especies:
            if(self.especie == esp):
                print(self.sound)
        pass
    def moverse():
        pass
class Perro(Animal):
    dog_name = ""
    age = 0
    def __init__(self, name, age) -> None:
        self.dog_name = name
        self.age = age
    
    def change_name(self):
        new_name = input("Escribe un nuevo nombre")
        self.dog_name = new_name
    def ladrar(self):
        print(f"Guau {self.dog_name} Guau")
    @staticmethod
    def call_dog():
        print("Metodo estatico")
mi_perro =  Perro("Pitty", 2)
mi_perro.ladrar()
print(Perro.__bases__)
# mi_perro.change_name()
# mi_perro.ladrar()
Perro.call_dog()

