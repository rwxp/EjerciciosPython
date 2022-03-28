## Hay un curso de natación que hace descuentos por edades:
## El valor del curso es de 800.000
## Dependiendo de la edad asigna un porcentaje de descuento.
## Para las personas menores o iguales de 6 años el descuento es del 50%
## Para las personas mayores de  6 años pero menores de edad el descuento es del 35%
## Para las personas mayores de edad el descuento es del 20% siempre y cuando tengan seguro de vida
## Para las personas mayores de 61 años el descuento es del 25% siempre y cuando tengan pensión, si no tienen pensión es del 20%.


valorCurso = 800000
valorFinal = 0
entrada = ""
descuento = 0
edad = 0

while(edad <= 0):
    try:
        edad = int(input("Por favor ingrese su edad:\n"))
    except:
        print("La edad que ingresó NO es correcta, inténtelo nuevamente.")
        edad = 0

if(edad <= 6):
    descuento = 50
elif(edad > 6 and edad < 18):
    descuento = 35
elif(edad >= 18) and edad <= 61:
    while(entrada != "S" and entrada != "s" and entrada != "N" and entrada != "n"):
      entrada = input("¿Tiene seguro de vida? (S/N)\n")
    if entrada == "S" or entrada =="s":
        descuento = 20
    entrada = ""
elif(edad > 61):
    while(entrada != "S" and entrada != "s" and entrada != "N" and entrada != "n"):
      entrada = input("¿Cuenta con pensión? (S/N)\n")
    if entrada == "S" or entrada == "s":
        descuento = 25
    else:
        descuento = 20
    entrada = ""


valorDescuento = valorCurso * (descuento/100)
valorFinal = valorCurso - valorDescuento

print("El valor final a pagar es de: " + str(valorFinal) + ".\nEl valor descontado es: " + str(valorDescuento))


