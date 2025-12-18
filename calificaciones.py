#Problema: Gestión básica de calificaciones de un grupo

#Contexto

#Un docente necesita un programa sencillo para registrar y consultar las calificaciones de un grupo de estudiantes. Cada grupo tendrá una lista de calificaciones y se deberán realizar operaciones básicas sobre dicha lista.

#Instrucciones

#1. Crea una clase llamada Grupo.


#2. La clase debe tener:

#Un constructor que reciba el nombre del grupo.

#Un atributo que almacene las calificaciones en una lista.

#Un método llamado agregar_calificacion que reciba una calificación y la agregue a la lista.

#Un método llamado mostrar_calificaciones que imprima todas las calificaciones junto con su posición (índice) en la lista.

#Un método llamado obtener_calificacion que reciba un índice y muestre la calificación correspondiente a esa posición.


#3. En el programa principal:

#Crea al menos un objeto de la clase Grupo.

#Agrega varias calificaciones.

#Consulta calificaciones usando distintos índices.

class Grupo:
    def __init__(self,nombregrupo):
        self.nombregrupo=nombregrupo
        self.calificaciones=[]
    
    def agregar_calificacion(self,calificacion):
        self.calificaciones.append(calificacion)    
    
    def mostrar_calificaciones(self):    
        print(f"Calificaciones del grupo: {self.nombregrupo}")
        elementos=len(self.calificaciones)
        for elemento in range (elementos):
            print(f"{elemento+1} {self.calificaciones[elemento]}")
    
    def obtener_calificacion(self,indice):
            print(f"Calificación en el índice {indice}: {self.calificaciones[indice-1]}")

grupo1=Grupo("Matemáticas")
grupo1.agregar_calificacion(85)
grupo1.agregar_calificacion(90)
grupo1.agregar_calificacion(78)
grupo1.agregar_calificacion(92)
grupo1.mostrar_calificaciones()

indice=int(input("Ingresa el índice de la calificación que deseas consultar: "))
grupo1.obtener_calificacion(indice)   