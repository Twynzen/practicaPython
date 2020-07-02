print('Bienvneidos a las historias clinicas del hospital un paso al infierno')
# * ****************** *
# * VARIABLES GLOBALES *
# * ****************** *
running = True
database = list()
# * ****************** *
# *      FUNCIONES     *
# * ****************** *
def showMenu():
    print("")
    print('MENU')
    print('1. Cargar paciente')
    print('2. Buscar paciente')
    print('3. Listar pacientes')
    print('4. Salir')
    print("")
    res = input('Ingrese una opción ->')
    return res

def responseValidation(r):
    validate = False
    num_res = 0

    if response.isdigit():
        num_res= int(response)
        if num_res >= 0 and num_res <= 4:
            msg = 'Esta en rango'
            validate = True
        else: 
            msg ='Fuera de rango'
    else:
         msg = 'Entrada incorrecta'
    
    return validate, num_res, msg 
# * ****************** *
# *   LOOP PRINCIPAL   *
# * ****************** *
while running:
   response = showMenu()
   validate, num_res, msg = responseValidation(response)
   print(validate, num_res, msg )
   