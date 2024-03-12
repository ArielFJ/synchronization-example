# Cuenta Bancaria Multihilo

| [Enlace vídeo](https://youtu.be/kgurFDZRr8s)

Este código en Python simula un escenario de operaciones bancarias concurrentes utilizando el módulo `threading` para gestionar hilos. La clase `CuentaBancaria` representa una cuenta bancaria con funciones para realizar transacciones de manera segura utilizando un objeto de bloqueo.

## Uso del Código

1. **Instanciar la Cuenta Bancaria:**
   ```python
   cuenta = CuentaBancaria(1000)
   ```

   Se crea una instancia de la clase `CuentaBancaria` con un saldo inicial de 1000.

2. **Realizar Transacciones:**
   ```python
   def realizar_transacciones(nombre_hilo):
       for _ in range(3):
           cuenta.realizar_transaccion(200, f"[{nombre_hilo}]")
   ```

   Se define la función `realizar_transacciones` que simula realizar varias transacciones desde diferentes ubicaciones. Cada transacción toma 200 unidades de la cuenta.

3. **Crear Hilos y Ejecutar Transacciones:**
   ```python
   hilo1 = threading.Thread(target=realizar_transacciones, args=['hilo1'])
   hilo2 = threading.Thread(target=realizar_transacciones, args=['hilo2'])

   hilo1.start()
   hilo2.start()

   hilo1.join()
   hilo2.join()
   ```

   Se crean dos hilos (`hilo1` y `hilo2`) que intentan realizar transacciones simultáneamente. Los hilos inician sus operaciones y se espera a que ambos terminen antes de continuar.

4. **Resultado:**
   ```
    [hilo1] Transacción exitosa. Saldo anterior: 1000, Nuevo saldo: 1200
    [hilo2] Transacción exitosa. Saldo anterior: 1000, Nuevo saldo: 1400
    [hilo1] Transacción exitosa. Saldo anterior: 1400, Nuevo saldo: 1600
    [hilo2] Transacción exitosa. Saldo anterior: 1400, Nuevo saldo: 1800
    [hilo1] Transacción exitosa. Saldo anterior: 1800, Nuevo saldo: 2000
    [hilo2] Transacción exitosa. Saldo anterior: 1800, Nuevo saldo: 2200
    Operaciones bancarias completadas.
   ```

   Las transacciones se realizan de manera segura, reflejando la sincronización efectiva del código para evitar conflictos en el acceso a la cuenta bancaria.

> Nota: Descomentar la línea `with self.bloqueo:` en el método `realizar_transaccion` para ver el efecto de la sincronización.