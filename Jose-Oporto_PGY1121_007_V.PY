import numpy as np

lotes = [["[]", "[]", "[X]", "[]", "[X]"],
         ["[X]", "[]", "[X]", "[]", "[]"],
         ["[]", "[]", "[]", "[]", "[]"],
         ["[]", "[X]", "[]", "[]", "[]"]]

matriz = np.array(lotes)
clientes = []

def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    print(matriz)

def seleccionar_lote():
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))

    if fila < 0 or fila >= matriz.shape[0] or columna < 0 or columna >= matriz.shape[1]:
        print("Ubicación inválida. Intente nuevamente.")
        return

    if matriz[fila, columna] == "[]":
        rut = input("Rut: ")
        nombre_completo = input("Nombre completo: ")
        telefono = input("Teléfono: ")
        correo = input("Email: ")

        lote_seleccionado = {
            "fila": fila,
            "columna": columna,
            "rut": rut,
            "nombre_completo": nombre_completo,
            "telefono": telefono,
            "correo": correo
        }

        clientes.append(lote_seleccionado)
        matriz[fila, columna] = "[X]"
        print("¡Lote seleccionado con éxito!")
    else:
        print("No puedes seleccionar este lote. Está vendido.")

def mostrar_detalles_lote_seleccionado():
    if len(clientes) == 0:
        print("No hay lotes seleccionados por clientes.")
    else:
        for cliente in clientes:
            fila = cliente["fila"]
            columna = cliente["columna"]
            numero_lote = (fila * matriz.shape[1]) + columna + 1
            print(f"Número lote: {numero_lote}")
            print("Tamaño: 5.000 m2")
            print("Detalles del cliente:")
            print(f"RUT: {cliente['rut']}")
            print(f"Nombre completo: {cliente['nombre_completo']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Email: {cliente['correo']}")
            print("------------------------")

def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay lotes seleccionados por clientes.")
    else:
        print("Clientes:")
        for cliente in clientes:
            print(f"RUT: {cliente['rut']}")
            print(f"Nombre completo: {cliente['nombre_completo']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Email: {cliente['correo']}")
            print("------------------------")

def mostrar_menu():
    print("Bienvenido a LoteosDuoc")
    while True:
        print("\nSeleccione una opción:")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver Clientes")
        print("5. Salir")
        opc = int(input())
        if opc == 1:
            mostrar_disponibilidad_lotes()
        elif opc == 2:
            seleccionar_lote()
        elif opc == 3:
            mostrar_detalles_lote_seleccionado()
        elif opc == 4:
            mostrar_clientes()
        elif opc == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Iniciar la aplicación
mostrar_menu()
