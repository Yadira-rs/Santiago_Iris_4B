#practica 1 Clases, Objetos y Atributos 

#Una clase que es una plantilla o un molde que define como sera un objeto 

class persona:
    def __init__(self, nombre, edad): # Constructor de una clase
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad}")
    
    def cumplir_años(self):
        self.edad += 1
        print(f"Esta persona Cumplio: {self.edad} años")
    

#Un objeto es una instancia creada a partir de cada clase
#crear objetos
estudiante1 = persona("Yadira", 19)
estudiante2 = persona("Lucia", 18)

#Asignar métodos a esos objetos (acciones)
estudiante1.presentarse()
estudiante2.presentarse()

#Paso 1. Agrega un método cumplir_años() que aumente en 1 la edad
estudiante1.cumplir_años()

#INSTANCIA:
#Cada objeto creado de una clase es una instancia, podemos tener varias instancias que coexistan con sus propios datos 
#Objeto = instancia de clase.
#Cada vez que se crea un objeto con Clase() se obtiene una instancia dependiente.
#Cada instancia tiene sus propias daros aunque vengan de la misma clase.

#Abstraccion 
#Representar solo lo importante del mundo real, ocultando detalles inecesarios.
class automovil:
    def __init__(self, marca):
        self.marca = marca
    def arrancar(self): 
        print(f"{self.marca} esta arrancando")

#crear un onjeto auto y asignar una marca 
auto = automovil("toyota")
auto.arrancar()
#Abstraccion: nos centramos solo en lo que importa (accion)
#que es arrancar un automovil, ocultando detalles internos 
#como motor, transmision, tipo_combustible.
#enfoque solo en la accion del objeto
#Objetivo es hacer el codigo mas limpio y facil de usar 


#-----Practica 1.2---------
#1. crear una clase mascotas  
#2. agregar minimo 4 atributos 
#3. definir al menos 4 metodos 
#4. crear 2 instancias de la clase 
#5. llamar los metodos y aplicar abstraccion: (agregar un atributo inncesario) 
#-----Practica 1.2---------

class Mascota:
    def __init__(self, nombre, especie, edad, color, numero_identificacion):  # numero_chip es el atributo innecesario
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
        self.numero_identificacion = numero_identificacion  # atributo innecesario para la abstracción

    def presentarse(self):
        print(f"Hola, esta mascota: {self.nombre}, un(a) {self.especie} de color {self.color} y tiene {self.edad} años.")

    def cumplir_años(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido años y  tiene {self.edad} años.")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau!")
        else:
            print(f"{self.nombre} hace un sonido diferente .")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"Y {self.nombre} es de color {self.color}.")
        
    def numero_identificacion(self):
        print(f"El nombre de mascota es {self.nombre} y su numero de indentificacion es {self.numero_identificacion}")
        
# Crear 2 instancias de la clase Mascota
mascota1 = Mascota("bimbo", "Perro", 3, "Marrón", "12345")
mascota2 = Mascota("dara", "Gato", 2, "Negro", "67890")

# Llamar los métodos
mascota1.presentarse()
mascota1.hacer_sonido()
mascota1.cumplir_años()
mascota1.cambiar_color("Blanco")

mascota2.presentarse()
mascota2.hacer_sonido()
