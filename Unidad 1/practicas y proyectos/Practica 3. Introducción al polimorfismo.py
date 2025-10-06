# Practica 3. Introducción al polimorfismo
# Simular un sistema de cobro con múltiples opciones de pago
# y mostrar notificaciones

class pago_tarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de {cantidad} con tarjeta."
    
class transferencia:
    def procesar_pago(self, cantidad):
        return f"Procesando pago por transferencia por la cantidad de {cantidad}."

class deposito: 
    def procesar_pago(self, cantidad): 
        return f"Procesando pago por depósito en ventanilla por la cantidad de {cantidad}."
    
class paypal:
    def procesar_pago(self, cantidad):
        return f"Procesando pago por medio de PayPal por la cantidad de ${cantidad}."



# CLASES DE NOTIFICACIÓN
class NotificacionCorreo:
    def enviar(self, mensaje):
        return f" Notificación enviada por correo electrónico: {mensaje}"

class NotificacionSMS:
    def enviar(self, mensaje):
        return f" Notificación enviada por SMS: {mensaje}"



# INSTANCIAS DE pagos 
pago1 = pago_tarjeta()
pago2 = deposito()
pago3 = transferencia()
pago4 = paypal()

# INSTANCIAS DE NOTIFICACIONES
correo = NotificacionCorreo()
sms = NotificacionSMS()


# POLIMORFISMO: PAGOS + NOTIFICACIONES
print(pago1.procesar_pago(100))
print(correo.enviar("Tu pago con tarjeta de $100 fue procesado con éxito."))

print(pago2.procesar_pago(400))
print(sms.enviar("Tu depósito de $400 fue recibido correctamente."))

print(pago3.procesar_pago(500))
print(correo.enviar("Tu transferencia de $500 fue completada."))

print(pago4.procesar_pago(2000))
print(sms.enviar("Tu pago por PayPal de $2000 fue confirmado."))





## Practica. Ejemplo de polimorfismo
# Simular un sistema de entrega con múltiples opciones
# Práctica: Polimorfismo con métodos de entrega + notificaciones

class entrega_domicilio:
    def entregar(self, producto):
        return f"Entregando {producto} directo a la dirección del cliente."

class entrega_tienda:
    def entregar(self, producto):
        return f"El cliente recogerá {producto} en la tienda."

class entrega_paquete:
    def entregar(self, producto):
        return f"{producto} se enviará por paquetería."

class entrega_digital:
    def entregar(self, producto):
        return f"{producto} fue entregado por correo electrónico."



# CLASES DE NOTIFICACIÓN
class NotificacionCorreo:
    def enviar(self, mensaje):
        return f" Notificación enviada por correo electrónico: {mensaje}"

class NotificacionSMS:
    def enviar(self, mensaje):
        return f" Notificación enviada por SMS: {mensaje}"



# INSTANCIAS
correo = NotificacionCorreo()
sms = NotificacionSMS()


# POLIMORFISMO: ENTREGAS + NOTIFICACIONES

print(entrega_domicilio().entregar("Laptop"))
print(correo.enviar("Tu Laptop ha sido enviada a tu domicilio."))

print(entrega_tienda().entregar("Celular"))
print(sms.enviar("Tu Celular está listo para recoger en tienda."))

print(entrega_paquete().entregar("Televisión"))
print(correo.enviar("Tu Televisión fue enviada por paquetería."))

print(entrega_digital().entregar("Software"))
print(sms.enviar("Tu Software fue entregado digitalmente por correo electrónico."))
