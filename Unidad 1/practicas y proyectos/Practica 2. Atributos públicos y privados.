# Practica 2. Atributos públicos y privados 

class Persona:
    def __init__(self, nombre, edad):  # Constructor de una clase
        self.nombre = nombre
        self.edad = edad
        self._cuenta = None  # atributo privado 

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    def cumplir_años(self):
        self.edad += 1
        print(f"{self.nombre} cumplió {self.edad} años.")

    def asignar_cuenta(self, cuenta):
        self._cuenta = cuenta 
        print(f"{self.nombre} ahora tiene una cuenta bancaria.") 

    def consultar_saldo(self):
        if self._cuenta:
            print(f"El saldo de {self.nombre} es: ${self._cuenta.mostrar_saldo()}")
        else: 
            print(f"{self.nombre} aún no tiene cuenta bancaria.")


class CuentaBancaria:
    def __init__(self, num_cuenta, saldo):  # corregido "__init__"
        self.num_cuenta = num_cuenta
        self._saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        return self._saldo 
        
    def depositar(self, cantidad): 
        if cantidad > 0: 
            self._saldo += cantidad 
            print(f"Se depositó la cantidad de ${cantidad}. Nuevo saldo: ${self._saldo}")
        else: 
            print("Ingresa una cantidad válida.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self._saldo:
                self._saldo -= cantidad
                print(f"Se retiraron ${cantidad}. Nuevo saldo: ${self._saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("Ingresa una cantidad válida.")


# Crear objetos o instancias de las clases 
persona1 = Persona("Miguel", 20)
cuenta1 = CuentaBancaria("001", 500)

# Asignar cuenta a la persona
persona1.asignar_cuenta(cuenta1)
persona1.consultar_saldo()

# Operaciones con la cuenta
cuenta1.depositar(200)
cuenta1.retirar(100)

# Acceso a atributos públicos
print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")
