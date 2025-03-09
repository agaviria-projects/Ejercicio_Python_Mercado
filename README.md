Este programa es una aplicación básica de lista de mercado en Python. Permite al usuario agregar productos a una lista, verlos, editarlos y eliminarlos. Sin embargo, tiene un problema crítico: todos los productos se almacenan en la misma referencia de diccionario producto, lo que hace que al agregar un nuevo producto, sobrescriba el anterior.

Explicación del código:
Inicializa variables

nombreVendedor = None: Variable sin uso en el programa.
productos = []: Lista donde se almacenarán los productos.
producto = {}: Diccionario para cada producto (pero mal usado, lo que genera errores).
Menú de opciones
Se imprime un menú con cinco opciones:

1️⃣ Crear lista de mercado
2️⃣ Ver lista de mercado (aún sin implementar)
3️⃣ Editar producto (sin implementar)
4️⃣ Eliminar producto (sin implementar)
5️⃣ Salir
Bucle while para interacción

Pide al usuario una opción.
Si elige 1, se le piden datos del producto y se agrega a productos.
