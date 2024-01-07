# importamos lo que necesitamos
from os import system
import os
import platform

# declaramos las clases
class Persona:

    # hacemos el constructor
    def __init__(self, nombre, apellido):
        
        self.nombre = nombre
        self.apellido = apellido

# esta clase hereda
class Cliente(Persona):

    # hacemos el constructor
    def __init__(self, nombre, apellido, num_cuenta, balance):

        # importamos el constructor padre
        super().__init__(nombre, apellido)

        self.num_cuenta = num_cuenta
        self.balance = balance

    # declaramos un metodo especial
    def __str__(self):

        return f'Bienvenido, \033[1m{self.nombre} {self.apellido}\033[0m\nA tu Banco \033[1mPruebas\033[0m \nTu cuenta es: \033[1m{self.num_cuenta}\033[0m \nTienes un saldo de \033[1m{self.balance:,.2f}\033[0m'
    
    # declaramos los metodos
    def depositar(self):

        # realizamos un bucle
        while True:
        
            # le pregunatamos al usuaria
            valor_agregado = input('\nCuanto deseas depositar en tu cuenta: ')

            # creamos una variable la cual contebdra lo que el usuario ha ingresado y reemplazamos los lugares de las , por cadenas vacias, en otras palabras eliminamos las ,
            valor_agregado_sin_comas = valor_agregado.replace(',', '')

            # hacemos la comprobacion de si es un digito y lo reemplazamos igual que la , pero ahora es un . y qeu tenga 2 decimales
            if valor_agregado.replace('.', '', 2).isdigit():

                # almacenamos en la variable el valor convertido a float
                valor_agregado = float(valor_agregado_sin_comas)

                break

            else: 

                # informamos al usuario
                print('\nDebes ingresar unicamente letras o numeros, intenta de nuevo')

        # suamos al balance lo agregado por el usuario
        self.balance += valor_agregado

        # retornamos el nuevo saldo formateado
        return f'\033[1m{self.nombre} {self.apellido}\033[0m tu nuevo Saldo es $ \033[1m{self.balance:,.2f}\033[0m'
    
    def retirar(self):

        # realizamos un bucle
        while True:
        
            # le pregunatamos al usuaria
            valor_retirado = input('\nCuanto deseas retirar de tu cuenta: ')

            # creamos una variable la cual contebdra lo que el usuario ha ingresado y reemplazamos los lugares de las , por cadenas vacias, en otras palabras eliminamos las ,
            valor_retirado_sin_comas = valor_retirado.replace(',', '')

            # hacemos la comprobacion de si es un digito y lo reemplazamos igual que la , pero ahora es un . y qeu tenga 2 decimales
            if valor_retirado.replace('.', '', 2).isdigit():

                # almacenamos en la variable el valor convertido a float
                valor_retirado = float(valor_retirado_sin_comas)

                break

            else: 

                # informamos al usuario
                print('\nDebes ingresar unicamente letras o numeros, intenta de nuevo')

        # comprobamos que el balance no sea mayor a lo solicitado por el usuario
        if self.balance >= valor_retirado:

            # resrtamos al balance lo agregado por el usuario
            self.balance -= valor_retirado

            # retornamos el nuevo saldo formateado
            return f'\033[1m{self.nombre} {self.apellido}\033[0m tu nuevo Saldo es $ \033[1m{self.balance:,.2f}\033[0m'
        
        else:

            # informamos al usuario
            print('\nNo tienes suficiente dinero para retirar esa cantidad')

class Salir_Sistema:

    # declaramos el metodo
    def salir(self):

        # informamos al usuario 
        print('\nHas salido del sistema, Hasta Pronto!')

        # salimos del sistema
        exit()

class LimpiarPantalla:

    # declaramos el constructr
    def __init__(self):
        
        # almacenamos el sistema operativo
        self.platform = platform.system()

    # declaramos un metodo
    def clear(self):

        # realizamos una comprobacion
        if self.platform == 'Windows':

            # limpiamos pantalla en windows
            os.system('cls')

        else:

            # limpiamos pantalla en otros sistemas
            os.system('clear')

# declaramos las funciones
def datos_personales():

    # creamos un bucle
    while True:
        
        # le pedimos al usuario que ingrese el nombre
        nombre = input('\nIngresa tu Nombre, por favor: ').title()

        # reemplazamos la variable eliminando los espacios en blanco, verificamos si todos son letras, verificamos si todos los caracteres son imprimibles
        if nombre.replace (' ','').isalpha() and nombre.isprintable():

            break

        else: 

            # informamas al usuario
            print('\nDebes ingresar unicamente letras, letras acentuadas y espacio si hay varios nombres, intenta de nuevo')

    # creamos un bucle
    while True:
        
        # le pedimos al usuario que ingrese el apellido
        apellido = input('\nIngresa tu Apellido, por favor: ').title()

        # reemplazamos la variable eliminando los espacios en blanco, verificamos si todos son letras, verificamos si todos los caracteres son imprimibles
        if apellido.replace (' ','').isalpha() and apellido.isprintable():

            break

        else: 

            # informamas al usuario
            print('\nDebes ingresar unicamente letras, letras acentuadas y espacio si hay varios apellidos, intenta de nuevo')
    

    # creamos un bucle
    while True:
        
        # le pedimos al usuario que ingrese el apellido
        num_cuenta = input('\nIngresa tu Número de cuenta, por favor: ').upper()

        # verficamos si lo ingresado es un número
        if num_cuenta.isalnum():

            break

        else: 

            # informamas al usuario
            print('\nDebes ingresar unicamente letras o numeros, intenta de nuevo')
    
    #retornamos las variables
    return nombre, apellido, num_cuenta

def crear_cliente():
    
    # en cada variable almacenaremso los datos ingresados por el usuario en la funcion datos_personales
    nombre, apellido, num_cuenta = datos_personales()

    # instanciamos la clase Cliente
    cliente = Cliente(nombre, apellido, num_cuenta, balance=0 )

    # retornamos el objeto
    return cliente

def entrada_al_sistema():

    # inicamos el odjeto vacio
    cliente = None

    # realizamos el menu en una lista
    menu = ['Datos del Cliente', 'Hacer Deposito', 'Hacer Retiro', 'Salir del Sistema']

    # creamso un bucle
    while True:

        # informamos al usuario
        print('\nElige una opción del siguiente \033[1mMenu:\033[0m\n')

        # recorremos la lista con un bucle
        for i, r in enumerate(menu, start=1):

            # imprimimos la lista
            print(f'{i} = {r}')

        # almacenamos la opcion elegida por el usuario
        opcion = input('\nElige una opción: ')

        # verificamos si es un número
        while not opcion.isnumeric():

            # informamos al usuario
            print('\nHas elegido una opcion invalida, intenta de nuevo')

            # pedimos nuevamente que ingrese la opcion
            opcion = input('\nElige una opción: ')

        # convertimos la opción a entero
        opcion = int(opcion)

        # realizamos una verificación
        if opcion -1 > len(menu):

            # informamos al usuario
            print('\nHas elegido una opcion invalida, intenta de nuevo')

        # opcion para salir del sistema
        elif opcion == 4:
            
            # instanciamos la clase LimpiarPantalla
            limpiar = LimpiarPantalla()

            # accedemos al método de la clase
            limpiar.clear()

            terminar = Salir_Sistema()

            terminar.salir()

        else:

            # verificamos cada opción del menú
            match opcion:

                case 1:

                    # verificamos si el cliente esta vacio
                    if cliente is None:

                        # creamos el cliente
                        cliente = crear_cliente()

                    else:

                        # instanciamos la clase LimpiarPantalla
                        limpiar = LimpiarPantalla()

                        # accedemos al método de la clase
                        limpiar.clear()

                        # informamos al usuario
                        print('\nYa ingresaste los datos del cliente')

                case 2:

                    # mostramos la información del cliente
                    print(str(cliente))

                    # verificamos si el cliente no esta vacio
                    if cliente is not None:

                        # mostramos la información para realizar depositos
                        print(cliente.depositar())

                    else:

                        # instanciamos la clase LimpiarPantalla
                        limpiar = LimpiarPantalla()

                        # accedemos al método de la clase
                        limpiar.clear()

                        # informamos al usuario
                        print('\nPrimero ingresa los datos del cliente')

                case 3:

                    # mostramos la información del cliente
                    print(str(cliente))

                    # verificamos si el cliente no esta vacio
                    if cliente is not None:

                        # mostramos la información para realizar retiros
                        print(cliente.retirar())

                    else:

                        # instanciamos la clase LimpiarPantalla
                        limpiar = LimpiarPantalla()

                        # accedemos al método de la clase
                        limpiar.clear()

                        # informamos al usuario
                        print('\nPrimero ingresa los datos del cliente')
                
                case _:

                    # instanciamos la clase LimpiarPantalla
                    limpiar = LimpiarPantalla()

                    # accedemos al método de la clase
                    limpiar.clear()

                    # informamos al usuario
                    print('\nHas elegido una opcion no valida, intenta de nuevo')

                    # para continuar dentro del bucle
                    continue

# llamamos a la funcion entrar al sistema
entrada_al_sistema()    