import funciones as func

contador_6lts = 0
contador_10lts = 0
contador_20lts = 0
registro = []

while True:
    print("Menu principal")
    print("1. Registrar pedido ")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Buscar un pedido por ID")
    print("5. Salir del programa")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("Registro de pedido")
        func.registro(registro)
        func.cantidad_cilindros(registro)
    elif opcion == "2":
        print("Listado de pedidos")
        func.listar(registro)
    elif opcion == "3":
        print("Imprimir hoja de ruta")
    elif opcion == "4":
        print("Búsqueda de pedido por ID")
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("La opcion ingresada es inválida. Intente nuevamente")


