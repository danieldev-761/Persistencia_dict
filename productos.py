# Sistema de gestión de productos
# Este programa permite agregar, ver y gestionar productos almacenados en un archivo de texto.

def guardar_productos(productos):
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for p in productos:
            linea = f"{p['id']}|{p['nombre']}|{p['precio']}\n"
            archivo.write(linea)


# Función para leer productos desde el archivo de texto
def leer_productos():
    # Inicializa una lista vacía para almacenar los productos
    productos = []

    try:
        # Intenta abrir el archivo productos.txt en modo lectura
        with open("productos.txt", "r", encoding="utf-8") as archivo:
            # Itera sobre cada línea del archivo
            for linea in archivo:
                # Divide la línea por el separador "|" y elimina espacios en blanco
                datos = linea.strip().split("|")

                # Crea un diccionario con los datos del producto
                producto = {
                    "id": int(datos[0]),  # Convierte el ID a entero
                    "nombre": datos[1],   # Nombre como string
                    "precio": float(datos[2])  # Convierte el precio a float
                }

                # Agrega el producto a la lista
                productos.append(producto)

    except FileNotFoundError:
        # Si el archivo no existe, simplemente pasa (no hace nada)
        pass

    # Retorna la lista de productos
    return productos


def sistema_productos():
    productos = leer_productos()

    # manejar ID automático
    if productos:
        id_actual = productos[-1]["id"] + 1
    else:
        id_actual = 1

    while True:
        print("\n1. Agregar producto")
        print("2. Ver productos")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))

            producto = {
                "id": id_actual,
                "nombre": nombre,
                "precio": precio
            }

            productos.append(producto)
            id_actual += 1

            guardar_productos(productos)
            print("Producto guardado ✔")

        elif opcion == "2":
            if productos:
                for p in productos:
                    print(f"{p['id']} - {p['nombre']} - ${p['precio']}")
            else:
                print("No hay productos")

        elif opcion == "3":
            break

        else:
            print("Opción inválida")


sistema_productos()