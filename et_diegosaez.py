productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    'GF75HD': [749990, 2],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

def stock_marca(marca):
    total = sum(stock.get(modelo, [0, 0])[1]
                for modelo, datos in productos.items()
                if datos[0].lower() == marca.lower())
    print(f"\nStock total disponible para {marca}: {total} unidades.\n")

def filtro_de_precios(minimo, maximo):
    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if minimo <= precio <= maximo and cantidad > 0 and modelo in productos:
            marca = productos[modelo][0]
            resultados.append(f"{marca} : {modelo} (${precio}) - {cantidad} unidades")
    if resultados:
        print(f"\nComputadores entre ${minimo} y ${maximo}:")
        for resultado in sorted(resultados):
            print("  -", resultado)
    else:
        print("\nNo se han encontrado computadores dentro del rango ingresado.\n")

def actualizacion_de_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        print(f"\nEl nuevo precio del modelo {modelo} es de ${nuevo_precio}.\n")
    else:
        print("\nEl modelo ingresado no existe en el stock.\n")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1) Ver stock por marca")
    print("2) Filtrar productos por precio")
    print("3) Actualizar precio de un producto")
    print("4) Salir")

    opcion = input("Ingrese su opción (1-4): ").strip()
    if opcion == "1":
        marca = input("Ingrese la marca a buscar: ").strip()
        stock_marca(marca)
    elif opcion == "2":
        try:
            minimo = int(input("Ingrese el valor mínimo de su búsqueda: "))
            maximo = int(input("Ingrese el valor máximo de su búsqueda: "))
            filtro_de_precios(minimo, maximo)
        except ValueError:
            print("\nDebe ingresar un número válido.\n")
    elif opcion == "3":
        modelo = input("Ingrese el modelo a actualizar: ").strip()
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio del modelo seleccionado: "))
            actualizacion_de_precio(modelo, nuevo_precio)
        except ValueError:
            print("\nIngrese un valor válido para el precio.\n")
    elif opcion == "4":
        print("\nSaliendo del programa... ¡Hasta pronto!")
        break
    else:
        print("\nOpción no válida. Por favor, elija entre 1 y 4.\n")
