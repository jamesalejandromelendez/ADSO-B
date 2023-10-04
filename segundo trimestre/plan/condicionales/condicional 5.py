"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
 y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
 Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos 
 los ingredientes que lleva."""
print("bienvenido al restaurante NN\n por favor elija el tipo de menu ")
tipo = input(" escirba 1 para escojer ingredientes vejetarianos  o  \n escirba 2 para escojer ingredientes no vejetarianos")
if tipo == "1":
    ingredientes = input("contamos con estos ingredientes:\npresiona 1 para pimenton\npresiona 2 para tofu")
    extras = input("lo prefiere con:\n-nozzarella\n-tomate\n=")
    if ingredientes == "1":
        print("escogiste pimenton con ",extras)
    if ingredientes == "2":
        print("escogiste tofu con ",extras)
    else:
        print("lo sentimos esta opcion no se encuentra dentro del menu")

if tipo == "2":
    ingredientes = input("contamos con estos ingredientes:\npresiona 1 para peperoni\npresiona 2 para jamon\npresiona 3 para salmon")
    extras = input("lo prefiere con:\n-nozzarella\n-tomate\n=")
    if ingredientes == "1":
        print("escogiste peperoni con ",extras)
    if ingredientes == "2":
        print("escogiste jamon con ",extras)
    if ingredientes == "3":
        print("escogiste salmon con ",extras)
    else:
        print("lo sentimos esta opcion no se encuentra dentro del menu")

     




 