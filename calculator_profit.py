def interest():
    print(f"""\nPerfecto {user_name}. Tenemos 3 tasas de interés anual para ti:
1. 14% anual
2. 8% anual
3. 5% anual""")
    interes = int(input('\nIngresa 1,2 o 3 según el tipo de ganancia que buscas: '))
    if interes == 1:
        interes = 0.14
        print(f'\n{user_name} has elegido el 14% anual.')
    elif interes == 2:
        interes = 0.08
        print(f"\n{user_name} has elegido el 8% anual. ")
    elif interes == 3:
        interes = 0.05
        print(f'\n{user_name} has elegido el 5% anual. ')
    else:
        print('\nDebes ingresar una opción válida: 1, 2 o 3. ')
        interest()
    return interes
        
def result():
    int2 = interest()
    mont2= monto
    for i in range(1,tiempo+1):
        mont2= round((mont2*int2)+mont2,2)
        print(f'> La ganancia del año {i} es de {mont2}.')

user_name=input('\t¡Hola! Bienvenido a Nuestro Banco.\n\n> Para poder registrarte ingresa tu nombre por favor: ')
monto= int(input(f'\nGracias por registrarte {user_name}.\n> Por favor ingresa el monto que estás dispuesto a ahorrar: '))
tiempo = int(input(f'\n> Por favor ingresa la cantidad de años que vas ahorrar los ${monto}: '))      
result()
