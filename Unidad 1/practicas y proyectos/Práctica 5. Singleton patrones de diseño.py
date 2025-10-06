# Practica 5. Patrones de diseño
# Singleton

class Logger: 
    # creamos un atributo de clase donde se aguardará la única instancia 
    _instancia = None 

    # __new__ es el método que controla la creación del objeto antes de init.
    # Sirve para asegurarnos de que solo exista una única instancia de la clase Logger 
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None: 
            cls._instancia = super().__new__(cls)
            # creamos atributo "archivo" que apunta a un archivo físico
            # "a" significa append = todo lo que se escriba se agrega al final del archivo
            cls._instancia.archivo = open("app.log", "a")
        return cls._instancia  # devolvemos siempre la misma instancia

    def log(self, mensaje):
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()  # asegura que se guarde en el disco

logger1 = Logger()  # primera y única instancia 
logger2 = Logger()  # devuelve la misma instancia

logger1.log("Inicio de sesión en la aplicación")
logger2.log("El usuario se autenticó")

# comprobar que son el mismo objeto en memoria
print(logger1 is logger2)


# Actividad de la práctica

class Presidente:
    _instancia = None  # 👈 faltaba declarar la variable de clase

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.historial = []
        return cls._instancia   # 👈 aquí estaba mal escrito (tenías __instancia)

    def accion(self, accion):  # 👈 corregido el nombre del método (antes "aacion")
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)

# Varios presidentes intentan tomar el poder 
p1 = Presidente("AMLO")
p2 = Presidente("Peña Nieto")
p3 = Presidente("Fox")

# Todos apuntan al mismo presidente 
p1.accion("firmó decreto")
p2.accion("visitó España")
p3.accion("aprobó un presupuesto")

print("\nHistorial del presidente")
print(p1.historial)

# Validación de Singleton
print(p1 is p2 is p3)  # True o False
