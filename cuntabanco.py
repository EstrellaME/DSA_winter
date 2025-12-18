#Problema: Control básico de una cuenta bancaria 
# Contexto

#Un banco necesita un programa sencillo para representar cuentas bancarias de sus clientes. Cada cuenta debe almacenar información básica y permitir realizar operaciones simples.

#Instrucciones

#1. Crea una clase llamada CuentaBancaria.


#2. La clase debe tener:

#Un constructor que reciba el nombre del titular y el saldo 

#Un método llamado mostrar_info que imprima el nombre del titular y el saldo actual.

#Un método llamado depositar que reciba una cantidad y la sume al saldo.

#Un método llamado retirar que reciba una cantidad y reste el monto del saldo solo si hay saldo suficiente.

#3. En el programa principal:

#Crea al menos dos objetos de la clase CuentaBancaria.

#Realiza depósitos y retiros en cada cuenta.

#Muestra la información final de cada cuenta usando mostrar_info.

class CuentaBancaria:
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self.saldo=saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print('Cantidad a depositar: '+ str(cantidad))
    
    def retirar(self, cantidad):
    
        if self.saldo < cantidad:
            print('Fondos insuficientes')
        else: 
            self.saldo-=cantidad
            print('Cantidad a retirar: '+ str(cantidad))

    def mostrar_info(self):
     print(f"{self.nombre} ,saldo actual: {self.saldo} ")

persona1=CuentaBancaria("Juan Lopez",200)       
persona2=CuentaBancaria("Sofia",400)

persona1.depositar(200)
persona1.retirar(100)
persona1.mostrar_info()

persona2.depositar(200)
persona2.retirar(100)
persona2.mostrar_info()