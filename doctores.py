from abc import ABC,abstractmethod 
import os

class medicos(ABC):
    def __init__(self, nom, ced, email, tel):
        self.nombre = nom
        self.cedula = ced
        self.correo = email
        self.telefono = tel
    
    @abstractmethod
    def mostrarusuarios(self):
        pass
    
class personal(medicos):
    def __init__(self, nom, ced, email, tel):
        super().__init__(nom, ced, email, tel)
        
        
    def mostrarusuarios(self):
        print(f"-"*15, "Personal", "-"*15) 
        print(f"Medico:",self.nombre, "", "Cedula:",self.cedula)
        

class paciente(medicos):
    def __init__(self, nom, ced, email, tel, genero, edad):
        super().__init__(nom, ced, email, tel)
        self.genero = genero
        self.edad = edad
        
    def mostrarusuarios(self):
        print(f"-"*15, "Paciente", "-"*15) 
        print(f"Paciente:",self.nombre, "", "Cedula:",self.cedula)
        
if __name__ == '__main__':
    
    
    os.system("cls")       
    med = personal("Anthony","0953758901","alopez@gmail.com","0962745197")
    med.mostrarusuarios()
    pac = paciente("Tizi","099999999","tizi@gmail.com","09999999","Femenino","21")
    pac.mostrarusuarios()