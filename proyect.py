import os
print('Bienvneidos a las historias clinicas del hospital un paso al infierno')
# * ****************** *
# * VARIABLES GLOBALES *
# * ****************** *
running = True
database = [{'nombre': 'Pepe', 'Clinica': 'Gripa'},
            {'nombre': 'VilGates', 'Clinica': 'Covid'},
            {'nombre': 'Lauro', 'Clinica': 'Porcino'}]
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
     res = input('Ingrese una opción -> ')
     os.system('clear')
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
     if validate:
         if num_res == 1:
             name = input("Ingrese el nombre del paciente: ")
             history = input("Ingrese la historia clinica del paciente: ")
             paciente = {'nombre':name, 'Clinica':history}
             database.append(paciente)
             print(database)
             
         elif num_res == 2:
             name = input("Ingrese el nombre del paciente: ")
             
             finded = True
             for x in range(len(database)):  
                 if  database[x]["nombre"].lower() == name.lower():
                     print("")
                     print( "Paciente encontrado | H. Clinica => ",database[x]["Clinica"])
                     print("")
                     finded = True
                     break
                 
                 else: 
                     finded = False
             if not finded:
                 print("Paila ya se murio")  
                        
         elif num_res == 3:
              print('* ****************** *')
              print('* LISTA DE PACIENTES *')
              print('* ****************** *')
              for x in range(len(database)):  
                 print("Nombre: ".ljust(10),database[x]["nombre"],"\tHistorial: ".ljust(10),database[x]["Clinica"])
         else: 
             print('* ****************** *')
             print('*     Finalizado     *')
             print('* ****************** *')
             running = False
               
     else: 
         print('* ****************** *')
         print('*     Finalizado     *')
         print('* ****************** *')