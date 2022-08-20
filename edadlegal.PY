edad = int(input("Digite su edad: "))

if(edad >= 0 and edad <= 14):
    print("Usted es niño")
elif(edad > 14 and edad <= 28):
    print("Usted es joven")
elif(edad > 28 and edad <= 60):
    print("Usted es adulto")
elif(edad > 60 and edad <= 105):
    print("Usted es adulto mayor")
elif(edad < 0 or edad >= 110):
    print("No se puede ingresar esa edad")
