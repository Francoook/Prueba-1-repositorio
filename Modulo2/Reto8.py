diccionario = {"amarillo": "yellow", "rojo":"reed", "azul": "blue" , "rosa":"pink"}
palabra1= input("Elija palabra a traducir: ")
if diccionario.get(palabra1) :
    print(palabra1,"=>" , diccionario.get(palabra1))
else:
    print("no tenemos la traduccion")

