
lista_compras = []

add = ""

while True:
    add = str(input("Que desea comprar? ([Q] para salir)\n"))
    if add == "Q" or add == "q":
        break

    confirmacion = str(input("Seguro que quieres añadir {} a la lista? [S/N]").format(add)).upper()
    if confirmacion == "S":
        lista_compras.append(add)
        print(lista_compras)
    else:
        print("No se añadio {} a la compra".format(add))
        print(lista_compras)
        continue

