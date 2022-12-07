"""9.5: Se dispone de un archivo STOCK correspondiente a la
existencia de artículos de un almacén y se desea señalar aquellos artículos cuyo nivel está por debajo del
mínimo y que visualicen un mensaje “hacer pedido”.
Cada artículo contiene un registro con los siguientes 
campos: número del código del artículo, nivel mínimo, nivel actual, proveedor, precio."""
almacen={"camiseta":{"codigo":1 ,"nivel minimo":5,"nivel actual":4,"proveedor":"alejandro","precio":20000}}
while True:
    nombre = input("nombre del articulo: ")
    if nombre == "":
        break
    c = int(input("codigo del articulo: "))
    m = int(input("nivel minimo: "))
    a = int(input("nivel actual: "))
    e = input("proveedor: ")
    p = int(input("precio: "))
    if a <= m:
        print("el nivel actual esta por debajo del minimo establecido")    
    articulo = {"codigo":c ,"nivel minimo":m,"nivel actual":a,"proveedor":e,"precio":p}
    almacen[nombre]=(articulo)
print(almacen)
B = input("desea consultar almacen? ")
if B == "si":
    for i,a in almacen.items():
        if a["nivel actual"]<a["nivel minimo"]:
            print("se nesecita 'HACER PEDIDO' de ",i)
        else:
            print("no se nesecitan pedidos de ",i)