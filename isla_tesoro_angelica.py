print("Bienvenido a la isla del tesoro")

desicion1 = input("¿Derecha o izquierda? \n")
if desicion1 == "izquierda":
    desicion2 = input("¿nadar o esperar? \n")
    if desicion2 == "esperar":
        desicion3_1 = input("¿cual puerta? \n")
        if desicion3_1 == "amarillo":
            print("¡GANASTE!")
        elif desicion3_1 == "azul":
            print("¡Deborado por bestias")
        elif desicion3_1 == "verde":
            print("MINIJUEGO")
            minijuego = input("¿ pasaste la etapa ? \n")
            if minijuego == "si":
                print("¡ Ganaste !")
        elif desicion3_1 == "rojo":
            print("¡Eres quemado GAME OVER!")
        else:
            print("opción incorrecta")
    elif desicion2 == "nadar":
        print("¡Ataque de la tribu! GAME OVER")
    else:
        print("opcion incorrecta")
        
    #elif desicion2 == "nadar":

elif desicion1 == "derecha":
    print("¡Caiste en un agujero! GAME OVER")
else:
    print("opción incorrecta")


