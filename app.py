import os, time
os.system("cls")

acceso = True
monto = 0
mes = 0
acumulador_depositos = 0
deposito = 0
cantidad_depositos = 0

while acceso:
    print("    Menú del Sistema")
    print("========= BANCO FINANCIERO =========")
    print("1. Mostrar cuotas de ahorro")
    print("2. Simular depósito acumulado")
    print("3. Tabla de crédito")
    print("4. Contar clientes atendidos")
    print("5. Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            print("1. Mostrar cuotas de ahorro")
            while monto <= 0:
                monto = int(input("Ingrese ahorro mensual: \n"))
                if monto <= 0:
                    print("el monto debe ser superior a 0")
            while mes <= 0:
                meses = int(input("Ingrese cantidad de meses\n"))
                if mes <= 0:
                    print("la cantidad debe ser superior a 0")
            #aca puedo seguir trabajando
            for x in range(1, meses + 1):
                ahorro_por_mes = monto * x
                print(f"Mes {x}: ${ahorro_por_mes}")
            time.sleep(2)
        elif opcion == 2:
            print("2. Simular depósito acumulado")
            while deposito >= 0:
                deposito = int(input("Ingrese depósito:\n"))
                acumulador_depositos = acumulador_depositos + deposito
                cantidad_depositos = cantidad_depositos + 1
                if deposito <= 0:
                    break
            print(f"Total acumulado en deposito: ${acumulador_depositos}")
            print(f"Cantidad de depositos: {cantidad_depositos}")
            time.sleep(2)
        elif opcion == 3:
            print("3. Tabla de crédito")
            monto_credito = int(input("Ingrese monto del crédito:\n"))
            if monto_credito > 0:
                print("Monto del crédito: $", monto_credito)
                for x in range(1,13):
                    resultado=monto_credito* x 
                    print(f"{monto_credito}x {x} = {resultado}")
        elif opcion == 4:
            print("4. Contar clientes atendidos")
            cant_clientes= int(input("Ingrese cantidad de clientes atendidos:\n"))
            print(f"Cantidad de clientes atendidos: {cant_clientes}")
        elif opcion == 5:
            print("Gracias por utilizar el sistema financiero")
            acceso = False
        else:
            print("Opción no válida")
    except:
        print("el valor debe ser numerico")
