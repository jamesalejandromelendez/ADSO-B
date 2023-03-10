
def agregar(productos):
    nombre = input("nombre del producto: ")
    precio = int(input("presio del producto: "))
    productos [nombre] = precio
    print(productos)
def comprar (productos,carro):
    producto = input("nombre del producto: ")
    for i,a in productos.items():
        if i == producto:
            print(i,'=', a)
            x = input ('desea comprar?\nresponde con un "si" o un "no"\n : ')
            if x=='si':
                carro[producto] = (a),
                print(carro)
def eliminar (productos):
    producto = input("que producto deseas eliminar? ")
    if producto in productos:
        del productos[producto]
        print(productos)
def devolucion (productos):
    u = input("que producto deseas devolver? ")
    if u in productos:
        for i,a in productos.items():
            if i == u:
                x = input('que desea?\n- 1 = cambio del producto\n- 2 = devolucion en efectivo')
                if x == "1":
                    print(comprar(productos))
                else:
                    print('su devolucion es de: ',a)




