import threading
import time

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.bloqueo = threading.Lock()

    def realizar_transaccion(self, cantidad, tag=''):
        with self.bloqueo:
            saldo_anterior = self.saldo
            time.sleep(1)  # Simulación de una operación que lleva tiempo
            self.saldo += cantidad
            nuevo_saldo = self.saldo
            print(f"{tag} Transacción exitosa. Saldo anterior: {saldo_anterior}, Nuevo saldo: {nuevo_saldo}")

# Crear una instancia de la cuenta bancaria con un saldo inicial
cuenta = CuentaBancaria(1000)

# Definir una función que simula realizar varias transacciones desde diferentes ubicaciones
def realizar_transacciones(nombre_hilo):
    for _ in range(3):
        cuenta.realizar_transaccion(200, f"[{nombre_hilo}]")

# Crear dos hilos que intentan realizar transacciones simultáneamente
hilo1 = threading.Thread(target=realizar_transacciones, args=['hilo1'])
hilo2 = threading.Thread(target=realizar_transacciones, args=['hilo2'])

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen antes de continuar
hilo1.join()
hilo2.join()

print("Operaciones bancarias completadas.")
