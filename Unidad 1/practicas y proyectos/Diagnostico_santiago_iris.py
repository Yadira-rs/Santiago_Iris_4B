# simulador de pedidos 
# conceptos basicos: variables, inputs, condicionales, funciones y bucles 

# elegir una tematica de tienda y escribir 3 productos 
productos = ["Dinamita", "Takis", "Ruffles"]
precios = [50, 70, 40]

# funcion para calcular total
def calcular_total(cantidad, precios):
    total = 0
    for i in range(len(cantidad)):
        total += cantidad[i] * precios[i]
    return total

# menu para usuarios (Outputs)    
print("Bienvenidos al menu de los snacks")
nombre = input("Ingresa tu nombre: ")

cantidad = []

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad_agregar = int(input(f"¿Cuántos {productos[i]} desea? "))
    cantidad.append(cantidad_agregar)

total = calcular_total(cantidad, precios)

# --- CICLO FOR PARA IMPRIMIR EL TICKET ---
print("\n--- TICKET DE COMPRA ---")
print(f"Cliente: {nombre}\n")
for i in range(len(productos)):
    if cantidad[i] > 0:  # solo mostrar lo que sí compró
        print(f"{productos[i]} x {cantidad[i]} = ${cantidad[i] * precios[i]}")
print(f"\nTOTAL A PAGAR: ${total}")
print("-------------------------")
print("¡Gracias por su compra!")
