#1. Crear una clase Ticket con los siguientes atributos:
#id
#tipo (por ejemplo: software, prueba)
#prioridad (alta, media, baja)
#estado (por defecto "pediente")
#2. Crear dos tickets de ejemplo y mostrar por pantalla
import os


class Ticket: 
    os.system("cls")
    def __init__(self, id, tipo, prioridad, estado="pendiente"):  # Constructor de una clase
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad  
        self.estado = estado

    def __str__(self):
        return f"Ticket {self.id} | Tipo: {self.tipo} | Prioridad: {self.prioridad} | Estado: {self.estado}"


class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre 

    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} está revisando el ticket {ticket.id}")


# Herencia
class Desarrollador(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "software":
            ticket.estado = "resuelto"
            print(f" El ticket {ticket.id} fue resuelto por el desarrollador {self.nombre}")
        else: 
            print(f" El desarrollador {self.nombre} no puede resolver este tipo de ticket.")


class Tester(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "prueba":
            ticket.estado = "validado"
            print(f" El ticket {ticket.id} fue validado por el tester {self.nombre}")
        else:
            print(f" El tester {self.nombre} no puede resolver este tipo de ticket.")


class ProjectManager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f" {self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)


# Crear algunos empleados
developer1 = Desarrollador("Gustavo")
tester1 = Tester("Pablo")
pm1 = ProjectManager("Susana")

# Lista global de tickets
tickets = []
contador_id = 1

#parte adicional
#agregar un menu con while y con if que permita: 
#1. crear un ticket 
#2. ver tickets
#3. asignar tickets
#4. salir del programa


# Menú
while True:
    print("\n--- MENÚ ---")
    print("1. Crear un ticket")
    print("2. Ver tickets")
    print("3. Asignar ticket")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tipo = input("Ingrese el tipo de ticket (software/prueba): ")
        prioridad = input("Ingrese la prioridad (alta/media/baja): ")
        nuevo_ticket = Ticket(contador_id, tipo, prioridad)
        tickets.append(nuevo_ticket)
        print(f" Ticket {contador_id} creado con éxito.")
        contador_id += 1

    elif opcion == "2":
        if tickets:
            print("\nLISTA DE TICKETS ")
            for t in tickets:
                print(t)
        else:
            print(" No hay tickets creados.")

    elif opcion == "3":
        if not tickets:
            print(" No hay tickets para asignar.")
            continue
        
        id_ticket = int(input("Ingrese el ID del ticket a asignar: "))
        encontrado = None
        for t in tickets:
            if t.id == id_ticket:
                encontrado = t
                break
        
        if not encontrado:
            print(" Ticket no encontrado.")
            continue

        print("Asignar a: 1) Desarrollador  2) Tester")
        emp_op = input("Elige: ")
        if emp_op == "1":
            pm1.asignar_ticket(encontrado, developer1)
        elif emp_op == "2":
            pm1.asignar_ticket(encontrado, tester1)
        else:
            print(" Opción inválida.")

    elif opcion == "4":
        print(" Saliendo del programa...")
        break

    else:
        print(" Opción no válida, intente de nuevo.")
