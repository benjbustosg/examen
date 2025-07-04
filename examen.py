def menu():
    while True:
        print("\n Menu Principal")
        print("1.- stock por marca")
        print("2.- buscar por el rango de precio")
        print("3.- actualizar precio modelo")
        print("4.- salir")
        opcion=input("ingrese una de las opciones: ")

        if opcion == "1":
            marca=input("ingrese la marca que desea consultar: ")
            stock_marca(marca)
        
        elif opcion == "2":
            try:
                precio_min=int(input("ingrese el precio minimo: "))
                precio_max=int(input("ingese el precio maximo: "))
                buscar_por_precio(precio_min, precio_max)
            except ValueError:
                print("debe ingresar un valor entero")

        elif opcion == "3":
            while True:
                modelo=input("ingrese un modelo de computadora que desea actualizar: ").strip().upper()
                try:
                    nuevo_precio=int(input("ingrese el nuevo valor: "))
                except ValueError:
                    print("debe ingresar un valor valido")
                    continue

                if actualizar_precio(modelo, nuevo_precio):
                    print("el precio se actualizo con exito")
                else:
                    print("el modelo no esta en nuestra base de datos")

                otro=input("desea actualizar otro precio (s/n): ").strip().lower()
                if otro != "5":
                    break
        
        elif opcion == "4":
            print("programa finalizado")
            break
        else:
            print("selecciona una opcion valida")


productos= {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == modelo.lower():
            total += stock.get(modelo, [0, 0])[1]
            print(f"el stock es: {total}")

def buscar_por_precio(precio_min, precio_max):
    disponibles=[]
    for modelo, (precio, cantidad) in stock.items():
        if precio_min <= precio <= precio_max and cantidad > 0:
            marca= productos[modelo][0]
            disponibles.append(f"{marca}--{modelo}")
    if disponibles:
        disponibles.sort()
        print(f"productos disponibles: {disponibles}")
    else:
        print("no hay computadores a este rango de precio")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    return False

menu()

