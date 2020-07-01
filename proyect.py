print('Bienvneidos a las historias clinicas del hospital un paso al infierno')
running = True

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

while running:
   response = showMenu()
   print('Respuesta del usuario ->  ',response)