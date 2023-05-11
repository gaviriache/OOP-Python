# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:38:05 2022

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
    
    def vec_pat(self):  #función para asignar en lista los valores electroencefalograficos
        # El retorno de la función será el arg del método libreria tabulate
        vec = [['Name', self.showName()], ['Id Card', self.showId()], ['Sexo', self.showSex()]]
        
        return vec
    
    def assignVec(self, sys, op):
        
        clinical_key = int(input('Write the clinical identication: '))
        var = sys.validation(clinical_key, op)  #op es un arg, para validar el numero de identificación de acuerdo a la opción escogida en el menú.
        name = input('Write the name of the patient: ')
        sex = str(input("Write the sex of patient: "))
        self.assignName(name), self.assignId(var), self.assignSex(sex)  #pat.assignId(arg) asigna el id validado.
        #función para optimizar código, invocar para crear un nuevo paciente y editar uno existente.
    
class Visit():
    
    
    def __init__(self):
        
        self.__date = date.today()
        self.__file = ''
        self.__notes = ''
        self.__index = []
        
        
    def showDate(self):        
        return self.__date
    
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
        file.write(self.showNotes() + os.linesep), file.close() # Finalización de escritura sobre el file. - close() fund.
        #....................................................................................................
        
    def showRegister(self, sys, num):  # mostrar contenido de datos almacenados en el archivo txt.
        var = sys.showRegs()
        if num in var.keys():
            vec = var[num]
            name_file = f'{vec[0]}.txt'
            self.__file = open(name_file, 'r')
            var = self.__file.read()
            self.__file.close()
            return var #  Load and print the file created with the information.
        
        else:
           return f'ID. Card is not registered into out files.' 
    #----------------------------   
    def assignNotes(self, notes): 
        
        self.__notes = notes
        
    def showNotes(self):        
        return self.__notes
    
    def assignIndex(self, index):        
        self.__index.append(index)
        
    def showIndex(self):        
        return self.__index
#----------------------------------------------------------

class Index():
    
   def __init__(self):
       
       self.__pot_delta = 0.0
       self.__pot_theta = 0.0
       self.__pot_alfa1 = 0.0
       self.__pot_alfa2 = 0.0
       self.__pot_beta = 0.0
       self.__pot_gamma = 0.0
       
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
       
   def vec_index(self):  
        # El retorno de la función será el arg del método libreria tabulate.
        
        vec =[['Potencia Delta', str(self.showDelta())], ['Potencia Theta', str(self.showTheta())], 
              ['Potencia Alfa 1', str(self.showAlfa_1())], ['Potencia Alfa 2', str(self.showAlfa_2())], 
              ['Potencia Beta', str(self.showBeta())], ['Potencia Gamma', str(self.showGamma())]]
               
        return vec
    
   def assignData(self):
             
       data = []  #vector store como arg de metodo assignIndex(data) en instancia Visit()
       delta, theta = float(input('Delta power: ')), float(input('Theta power: ')),
       alfa1, alfa2 = float(input('Alfa1 power: ')), float(input('Alfa2 power: ')), 
       beta, gamma = float(input('Beta power: ')),float(input('Gamma power: ')),
       data.append(delta), data.append(theta), data.append(alfa1)  #pendiente por implementación
       data.append(alfa2), data.append(beta), data.append(gamma) 
       self.assignDelta(delta), self.assignTheta(theta), self.assignAlfa_1(alfa1)
       self.assignAlfa_2(alfa2), self.assignBeta(beta), self.assignGamma(gamma)
    
       return data
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
       
class System():
    
    def __init__(self):
        
        self.__regs = {}
        
    def showRegs(self):
        return self.__regs
        
    def loadFile(self, visit, num):  #Load the file and print it on screen.  #pendiente validar id.
        
        return visit.showRegister(self, num)
    
    def validation(self, num, op):
        
        if op == 1:
            for k in self.__regs.keys():
            
                if int(k) == int(num):
                    
                    num = int(input("The ID. Card already exist, please verify and try again: "))
                    self.validation(num, op)
        
            return num  #nueva ID card para ser asignada a objeto patient.
        
        elif op == 2:    
            return num
            
        else:
            num = int(input("The ID-Card provided doesn´t exist into our files, verify and try again: "))
            self.validation(num, op)  #function recursive.
                
    
    def assignData(self, pat, visit, index): #pendiente
        
        self.__regs[int(pat.showId())] = [pat.showName(), pat.showId(), pat.showSex(), 
                    visit.showNotes(), visit.showIndex()]   
        
#    def showData(self, num):
#        
#        if num in self.__regs.keys():
#            return tabulate(self.__regs[num], headers=f'Id Card: {num}')
#            
#        else:
#            print('The identification provided doesn´t exist in our files.')
#            num = int(input('Verify and write again the Id Card. for showing the data'))
#            self.showData(num)
    
    def deletePat(self, num):  #func. delete registro en hash_dict and file.txt.
        
        if num in self.__regs.keys():
            var = self.__regs[num]  #get name asociated with the identification to delete name file
            name_file = f'{var[0]}.txt'
            os.remove(name_file)  #método libreria os para eliminar archivos.
            del self.__regs[num]
            
            return f'The patient has been deleted of our files system.'
        else:
            return f'The ID. Card -- {num} doesn´t exist into our files system.'
            
    
    def editData(self, pat, visit, index, num):
        
        if num in self.__regs.keys():
                        
            while True:
                option = int(input('''\nSelect an option for editing the data of diagnosis file:      
                             \n1 - Edit Identification data (Name, Id card, sex).
                             \n2 - Edit Index data of brain diagnosis file.
                             \n3 - Exit \nPlease tap one the options before: '''))
                
                if option == 1:
                    #sys.assignData(pat, vis, index) revisar.
                    pat.assignVec(self, num)  #re-definir los datos basicos de identificación
                    pat.vec_pat()  #invocar función para actualizar datos y re-asignarlos de nuevo al file
                    visit.assignRegister(pat, index)
                    
                elif option == 2:
                                       
                    index.assignData()  #re-definir los datos basicos de identificación
                    index.vec_index()  #invocar función para actualizar indices y re-asignarlos de nuevo al file
                    visit.assignNotes(str(input("Section of diagnosis notes provided by the technical adviser: ")))
                    visit.assignRegister(pat, index)
                                   
                else:
                    break                  
        
        else:
            num = int(input('The ID. Card isn´t into our files, verify again for showing data: '))
            self.editData(pat, visit, index, num)
#---------------------------------------    
sys = System()
while True:
    option = int(input('''\nSelect an option for Brain diagnosis file:      
                 \n1 - Create a clinical profile of Brain diagnosis.
                 \n2 - Edit the clinical data of a patient.
                 \n3 - Delete patient of the system.
                 \n4 - Load and print the diagnosis file.
                 \n5 - Get a view of the Patient´s data.
                 \n6 - Exit \nPlease tap one the options before: '''))
        
    if option == 1:
        
        pat = Patient()  #Instancia de la clase Paciente
        pat.assignVec(sys, option)
        index = Index()  #Instancia de la clase Index
        data = index.assignData()
        #pendiente bucle para número de visitas.
        vis = Visit()  #Instancia de la clase Visit  pendiente
        notes = str(input("Section of diagnosis notes provided by the technical adviser: "))
        vis.assignNotes(notes) #notas ingresadas por el tecnico de servicio
        vis.assignRegister(pat, index), vis.assignIndex(data), #segunda instrucción asigna el visita() vector de Index()
        sys.assignData(pat, vis, index)  #Add data into hash_dict del objeto System() besides of the file.txt
                
    elif option == 2:
         clinical_key = int(input(os.linesep + 'Write the clinical identication: '))
         sys.editData(pat, vis, index, clinical_key)
         
    elif option == 3:
         clinical_key = int(input(os.linesep + 'Enter the ID. Card of Patient: '))
         print (os.linesep + sys.deletePat(clinical_key))       
         
    elif option == 4:
        clinical_key = int(input(os.linesep + 'Enter the ID. Card of Patient: '))
        print (sys.loadFile(vis, clinical_key))
        
    elif option == 5:
        clinical_key = int(input(os.linesep + 'Write the clinical identication: '))
        print (sys.showData(clinical_key))  #Data update after execute method sys.editDdata
        
        
    elif option == 6:
        
        break
    
    
    
            
        
        
        
            
        
        
        
        
                
                
        
        