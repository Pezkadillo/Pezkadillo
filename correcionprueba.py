def dcto(total):
    if total >= 15000:
        total = round(total * 0.9)
    else:
        print("No aplica descuento")
    return total

def valida_menu():
    flag = True
    opt = input("Ingrese un nivel de picante: ")
    while flag:
        if opt == "1" or opt == "2" or opt == "3" :
            print("La Opcion es correcta")
            flag = False
        else:
            print ("La opcion es incorrecta")
            opt = input("Ingrese un nivel de picante: ")
    return opt#para llamar la opcion de picante
# print("Llamamos a la funcion valida menu")
# picante = valida_menu()
# print("Cunato picante quiere", picante)
# print(type(picante))

total_compra = 5000
print(dcto(total_compra))

