# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:48:05 2022

Algoritmo de creación de registros electroencefalográficos.

Luis Miguel Gaviria C. - Informática II - 12:14
"""

from datetime import date
import os
from tabulate import tabulate  #Profesor en el prompt escribir: pip install tabulate

class Patient():
    
    def __init__(self):
        
        self.__name = ''
        self.__id = 0
        self.__sex = ''
                        
    def assignName(self, name):         
        self.__name = name
        
    def showName(self):        
        return self.__name
        
    def assignId(self, num):        
        self.__id = num
        
    def showId(self):        
        return self.__id
    
    def assignSex(self, sex):         
       self.__sex = sex
        
    def showSex(self):         
        return self.__sex
    
    def assignVec(self, num):  # num: arg validado que será la identificación del objeto paciente.
        
        name = input('Write the name of the patient: ')
        sex = str(input("Write the sex of patient: "))
        self.assignName(name), self.assignId(num), self.assignSex(sex)  #pat.assignId(num) asigna el Id validado.
        #función para optimizar código, invocar para crear un nuevo paciente y editar uno existente.
   
    def vec_pat(self):  #func. asigna datos personales a vector.
        # El retorno de la función será el arg. del método libreria tabulate.
        vec = [['Name', self.showName()], ['Identification', self.showId()], ['Sexo', self.showSex()]]
        
        return vec
#----------------------------
    
class Visit():    
    
    def __init__(self):
        
        self.__date = date.today()
        self.__file = ''
        self.__notes = ''
        self.__index = []
                
    def showDate(self):        
        return self.__date
#..................................................................................
        
    def assignNotes(self, notes): 
        
        self.__notes = notes
        
    def showNotes(self):        
        return self.__notes
    
    def assignIndex(self, index):        
        self.__index.append(index.showData())
        
    def showIndex(self):  #func return list with Index() instancia.
        #ejecutar index.assignData() antes de index.showData()
        return self.__index
    
    def assignRegister(self, pat, index): #arg: objeto Patient - método será invocado desde el obj sys método save
        #func para crear registro de texto con la data del paciente. - Uso de librerias os y tabulate.
        self.__file = f'{pat.showName()}.txt'
        file = open(self.__file, 'w')  #sobre.escribe texto en el archivo, cursor al final.
        file.write(os.linesep + '\nRegistro Electroencefalográfico.\n--------------------------------\n' + os.linesep)
        file.write('Date:    ' + str(self.__date) + os.linesep)
        file.write(tabulate(pat.vec_pat(), tablefmt='grid') + os.linesep)
        file.write('\n------------------------------\nINDICES ELECTROENCEFALOGRÁFICOS:\n................................')
        file.write(os.linesep + tabulate(index.vec_index(), tablefmt='grid') + os.linesep)
        file.write('\n-------------------------------\nNotas tecnicas del diagnóstico:\n...............................' + os.linesep)
        file.write(self.showNotes() + os.linesep), file.close() # Finalización de escritura sobre el file. - close()
        #....................................................................................................
        
    def showRegister(self, sys, num):  # mostrar contenido de datos almacenados en el archivo txt.
        
        var = sys.saveRegs()
        vec = var[num]
        name_file = f'{vec[0].showName()}.txt'
        self.__file = open(name_file, 'r')
        var = self.__file.read()
        self.__file.close()
        return var #  Load and print the file created with the information.    
        
#----------------------------------------------------------........................

class Index():
    
   def __init__(self):
       
       self.__pot_delta = 0.0
       self.__pot_theta = 0.0
       self.__pot_alfa1 = 0.0
       self.__pot_alfa2 = 0.0
       self.__pot_beta = 0.0
       self.__pot_gamma = 0.0
       self.__data = []
       
   def assignDelta(self, delta):       
       self.__pot_delta = delta
       
   def assignTheta(self, theta):               
       self.__pot_theta = theta

   def assignAlfa_1(self, alfa1):              
       self.__pot_alfa1 = alfa1

   def assignAlfa_2(self, alfa2):        
       self.__pot_alfa2 = alfa2
       
   def assignBeta(self, beta):       
       self.__pot_beta = beta
       
   def assignGamma(self, gamma):       
       self.__pot_gamma = gamma
       
   #----------------------------    
   def showDelta(self):       
       return self.__pot_delta
   
   def showTheta(self):
       return self.__pot_theta
   
   def showAlfa_1(self):
       return self.__pot_alfa1
   
   def showAlfa_2(self):
       return self.__pot_alfa2
   
   def showBeta(self):
       return self.__pot_beta

   def showGamma(self):
       return self.__pot_gamma
#..................................
   def showData(self):
       self.__data.append(self.showDelta()), self.__data.append(self.showTheta()), self.__data.append(self.showAlfa_1())
       self.__data.append(self.showAlfa_2()), self.__data.append(self.showBeta()), self.__data.append(self.showGamma())     
                      
       return self.__data
    
   def assignData(self):
             
       delta, theta, alfa1 = float(input(os.linesep + 'Delta power: ')), float(input('Theta power: ')), float(input('Alfa-1 power: '))
       alfa2, beta, gamma  = float(input('Alfa-2 power: ')), float(input('Beta power: ')), float(input('Gamma power: '))
       self.assignDelta(delta), self.assignTheta(theta), self.assignAlfa_1(alfa1)
       self.assignAlfa_2(alfa2), self.assignBeta(beta), self.assignGamma(gamma)
       
   def vec_index(self): 
        # El retorno de la función será el arg del método libreria tabulate
       vec =[['Potencia Delta', str(self.showDelta())], ['Potencia Theta', str(self.showTheta())], 
             ['Potencia Alfa 1', str(self.showAlfa_1())], ['Potencia Alfa 2', str(self.showAlfa_2())], 
             ['Potencia Beta', str(self.showBeta())], ['Potencia Gamma', str(self.showGamma())]]
                   
       return vec
#-........................................................................................................................
class System():
    
    def __init__(self):
        
        self.__regs = {}
        
    def saveRegs(self):
        return self.__regs
    
    def assignData(self, pat, visit, index): #pendiente
          
        self.__regs[pat.showId()] = [pat, visit, index]
    #-------------------------------------------    
    def editData(self, num):
        
        var_object = self.__regs[num]  #local var func, lista de objetos pat, visit, index vinculados al id.
        while True:
            option = int(input('''\nSelect an option for editing the data of diagnosis file:      
                             \n1 - Edit Identification data (Name, Id card, sex).
                             \n2 - Edit Index data of brain diagnosis file.
                             \n3 - Exit \nPlease tap one the options before: '''))
                
            if option == 1:
                
                name_file = f'{var_object[0].showName()}.txt'
                os.remove(name_file)
                var_object[0].assignVec(num)  #re-definir los datos basicos de identificación
                var_object[0].vec_pat()  #invocar función para actualizar datos personales.
                var_object[1].assignRegister(var_object[0], var_object[2])
                    
            elif option == 2:
                
                name_file = f'{var_object[0].showName()}.txt'
                os.remove(name_file)                      
                var_object[2].assignData()  #re-definir los datos basicos de identificación
                var_object[2].vec_index()  #invocar función para actualizar datos electroencefalográficos.
                var_object[1].assignNotes(str(input("Section of diagnosis notes provided by the technical adviser: ")))
                var_object[1].assignRegister(var_object[0], var_object[2])
                # verificar                   
            else:
                break  
        self.assignData(var_object[0], var_object[1], var_object[2])  #invocar func. para actualizar registro en base de datos dict_hash.
          
        return True
    #------------------------------------------------------------------------------    
    def deletePat(self, num):  #func. delete registro en hash_dict and file.txt.
        
        if num in self.__regs.keys():
            var = self.__regs[num]  #get name asociated with the identification to delete name file
            name_file = f'{var[0].showName()}.txt'
            os.remove(name_file)  #método libreria os para eliminar archivos.
            del self.__regs[num]  #método dict_hash para eliminar clave:valor
            
            return f'The patient has been deleted of our files system.'
        else:
            return f'The ID. Card -- {num} doesn´t exist into our files system.'
     #------------------------------------------------------------------------------    
        
    def loadFile(self, visit, num):  #Load the file and print it on screen.  #pendiente validar id.
             
        return visit.showRegister(self, num)
    
    def validation(self, num, op):  #método validar para crear nuevo paciente./ Editar patient existente.
        
        if op == 1:  #validación para crear objeto paciente.
            if num in self.__regs.keys():
                num = int(input(os.linesep + "The ID. Card already exist, please verify and try again: "))
                self.validation(num, op)
            
            return num  # ID validado para ser asignada a objeto patient. 
        
        if op == 2:  #validar id para editar o consultar patient existente.
            
            if num in self.__regs.keys():
                pass
            else:
                num = int(input(os.linesep + "The ID was not found in our files, verify and write again: "))
                self.validation(num, op)  #func. recursiva.
            
            return num
sys = System()
while True:
    
    option = int(input('''\nSelect an option for Brain diagnosis file:      
                 \n1 - Create a clinical profile of Brain diagnosis.
                 \n2 - Edit the clinical data of a patient.
                 \n3 - Delete patient of the system.
                 \n4 - Load and print the diagnosis file.
                 \n5 - Exit \nPlease tap one the options before: '''))
        
    if option == 1:
           
        pat = Patient()  #Instancia de la clase Paciente
        clinical_key = int(input(os.linesep + 'Write the clinical identication: '))
        var = sys.validation(clinical_key, option)
        pat.assignVec(var)
        index = Index()  #Instancia de la clase Index
        index.assignData()
        #pendiente bucle para número de visitas.
        vis = Visit()  #Instancia de la clase Visit  pendiente
        vis.assignIndex(index)  #Object Index store in array of visit().
        notes = str(input("Section of diagnosis notes provided by the technical adviser: "))
        vis.assignNotes(notes) #notas ingresadas por el tecnico de servicio
        sys.assignData(pat, vis, index)  #Add data into hash_dict del objeto System() besides of the file.txt
        vis.assignRegister(pat, index) #segunda instrucción asigna el visita() vector de Index()
        
        
    elif option == 2:  
        
        clinical_key = int(input(os.linesep + 'Write the clinical identication: '))
        var = sys.validation(clinical_key, option)   #func, recibe var validada 
        bol = sys.editData(var)
        if bol is True:
            print (f'The information associated with the ID: {var} has been modified succesfully')
        else:
            continue
        
            
        '''continuar en linea 218 - definir dentro de la función las instrucciones para generar el nuevo archvio
        post-modificación y eliminar el antiguo. Eres un master, il bambino d´oro.'''    
            
    elif option == 3:
        
        clinical_key = int(input(os.linesep + 'Write the clinical identication: '))
        var = sys.deletePat(clinical_key)  
        print (var)  
        
    elif option == 4:
        
        clinical_key = int(input(os.linesep + 'Write the clinical identication: '))
        var = sys.validation(clinical_key, 2)   #func, recibe var validada 
        print (sys.loadFile(vis, var))
        
    else:
        break


# if __main__ == '__main__':    
    
   
