menu =""""
Bienvenido al conversor de monedas

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos
"""
def valores():
    
    pesos = float(pesos_c)
    valor_dolar=valor_dolar_paises
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares") 



opcion=int(input(menu))
if opcion ==1:
    pesos_c = input("Cuantos pesos Colombianos tienes?")
    valor_dolar_paises=3875
    valores()
elif opcion ==2:
    pesos_c = input("Cuantos pesos Argentinos tienes?")
    valor_dolar_paises=70
    valores()
elif opcion ==3:
    pesos_c = input("Cuantos pesos Mexicanos tienes?")
    valor_dolar_paises=24
    valores()

else:
    print("Ingresa un numero correcto:")