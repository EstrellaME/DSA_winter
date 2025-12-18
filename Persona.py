class Persona:
    #Constructor
    def __init__(self, nombre, edad):
    #Atributos    
        self.nombre = nombre
        self.edad = edad
    #Métodos
    def saludar(self):
      print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def es_mayor_de_edad(self):
     return self.edad >= 18
    
Persona1 = Persona("Juan López", 28)
Persona2 = Persona("Luis Rivas", 16)

Persona1.saludar()
Persona2.saludar()
print(Persona1.es_mayor_de_edad())
print(Persona2.es_mayor_de_edad())