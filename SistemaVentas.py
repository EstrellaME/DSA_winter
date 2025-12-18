#Problema: Sistema básico de ventas por vendedor

#Contexto

#Una empresa desea llevar el control de sus vendedores y las ventas realizadas por cada uno durante el día. Cada vendedor tiene múltiples ventas registradas y se necesita obtener información básica a partir de estos datos.

#Estructura de datos esperada

#Se utilizará un diccionario donde:

#Clave: nombre del vendedor (string).

#Valor: lista de montos de ventas (lista de números).

#Instrucciones

#1. Crea una clase llamada SistemaVentas.


#2. La clase debe tener:

#Un constructor que inicialice un diccionario vacío de vendedores.

#Un método agregar_vendedor que reciba el nombre del vendedor y lo agregue al sistema con una lista vacía de ventas.

#Un método registrar_venta que reciba el nombre del vendedor y el monto de la venta, y agregue el monto a su lista correspondiente.

#Un método mostrar_ventas que muestre cada vendedor con todas sus ventas.

#Un método total_vendedor que reciba el nombre de un vendedor y muestre el total de ventas realizadas (calculado manualmente).

#Un método mejor_vendedor que determine y muestre el nombre del vendedor con mayor total de ventas.

#3. En el programa principal:

#Registra varios vendedores.

#Agrega múltiples ventas a cada vendedor.

#Muestra todas las ventas.

#Muestra el vendedor con mayores ventas.

class SistemaVentas:
    def __init__(self):
        self.vendedores={}

    def agregar_vendedor(self,nombre):
        self.vendedores[nombre]=[]

    def registrar_venta(self,nombre,monto):
        if nombre in self.vendedores:
            self.vendedores[nombre].append(monto)

    def mostrar_ventas(self):
        for nombre in self.vendedores:
            print(f"{nombre}: {self.vendedores[nombre]}")

    def total_vendedor(self,nombre):
        if nombre in self.vendedores:
            total=0
            for venta in self.vendedores[nombre]:
                total+=venta
            print(f"Total ventas de {nombre}: {total}")

    def mejor_vendedor(self):
        mejor_nombre=""
        mejor_total=0
        for nombre in self.vendedores:
            total=0
            for venta in self.vendedores[nombre]:
                total+=venta
            if total>mejor_total:
                mejor_total=total
                mejor_nombre=nombre
        print(f"Mejor vendedor: {mejor_nombre} con ventas totales de {mejor_total}")

sistema=SistemaVentas()
sistema.agregar_vendedor("Juan")
sistema.agregar_vendedor("Maria")
sistema.agregar_vendedor("Luis")

sistema.registrar_venta("Juan", 150.0)
sistema.registrar_venta("Juan", 200.0)
sistema.registrar_venta("Maria", 300.0)
sistema.registrar_venta("Maria", 100.0)
sistema.registrar_venta("Luis", 250.0)
sistema.registrar_venta("Luis", 400.0)

sistema.mostrar_ventas()
sistema.total_vendedor("Juan")

sistema.total_vendedor("Maria")
sistema.total_vendedor("Luis")
sistema.mejor_vendedor()