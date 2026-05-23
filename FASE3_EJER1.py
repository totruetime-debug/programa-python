#CARLOS EDUARDO VANEGAS REDONDO
#1.125.231324
#Ejercio 1
#CODIGO FUENTE: Autoria Propia

# Ejercicio 1

i = 1

print()
print()
print("*** MONITOREO DE TEMPERATURA DE HORNO ***")
print()
print()

while i == 1:
    print("######################################################")
    print()    
    temperatura_horno = int (input("Ingrese la temperatura del horno en °C -->  "))
    print()
    print()
    if temperatura_horno > 0:
        if temperatura_horno < 180:
            print("Alerta: enfriamiento")
            print()
            print()
            i = int (input("¿Desea continuar? (1: sí, 0: no) -->  "))              
        elif temperatura_horno > 200:
            print("Alerta: calentamiento")
            print()
            print()
            i = int (input("¿Desea continuar? (1: sí, 0: no) -->  "))  
        else:
            print("Temperatura óptima")
            print()
            print()
            i = int (input("¿Desea continuar? (1: sí, 0: no) -->  "))          
    else :
        temperatura_horno = int (input("Ingrese una temperatura valida del horno en °C --> 4"))
    print()
    
    if i == 0:
        print()
    elif i == 1:
        print()
    else:
        while i > 1:
            i = int (input("¿Desea continuar? (1: sí, 0: no) -->  ")) 
    
else: 
    print("Monitoreo Finalizado")