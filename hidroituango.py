#Entradas del problema
nivelAgua = int(input("Digita el nivel de agua de la presa: "))

#Proceso del problema
if(nivelAgua >= 0 and nivelAgua < 20):
    print(f'el nivel de agua {nivelAgua} es muy bajo')
elif(nivelAgua >= 20 and nivelAgua < 400):
    print(f'el nivel de agua es optimo')
elif(nivelAgua >= 400):
    print(f'El nivel de agua es peligro')
else:
    print(f'Digite una opcion valida')