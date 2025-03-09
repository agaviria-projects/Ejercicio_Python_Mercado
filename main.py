#software estructuras
nombreVendedor = None

productos=[]
producto={}

#Creando un ciclo en python
opcion=100
print ("*** Merqueo APP ***")
print("1. Crear lista de mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("5. Salir")

while opcion != 5:
    opcion =int(input("Digita una opcion: "))
    if opcion==1 :
        print("Bienevnido a la creacion de tu lista de mercado")

        #Creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto:")
        producto["precio"]=int(input("Digita el precio del producto:"))
        producto["cantidad"]=int(input("cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("cual presentación llevaras? ")

        #mostrando mi diccionario
        #print(producto)

        #poblando una lista(agregando elementos a una lista)
        productos.append(producto)
        print(productos)
        

    elif opcion==2 :
        print("opcion 2")
    elif opcion==3 :
        print("opcion 3")
    elif opcion==4 :
        print("opcion 4")
    else:
        print("Opcion invalida")