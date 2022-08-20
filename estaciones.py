mesAño = input("Escriba el mes del año en el que esta(escribalo en letras minusculas)").lower()

if(mesAño == 'enero' or mesAño == 'febrero' or mesAño == 'marzo'):
    print("Usted esta en verano")
elif(mesAño == 'abril' or mesAño == 'mayo' or mesAño == 'junio'):
    print("Usted esta en primavera")
elif(mesAño == 'julio' or mesAño == 'agosto' or mesAño == 'septiembre'):
    print("Usted esta en verano")
elif(mesAño == 'octubre' or mesAño == 'noviembre' or mesAño == 'diciembre'):
    print("Usted esta en otoño")
else:
    print(f'{mesAño} no es un mes del año')
