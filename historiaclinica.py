import os

class hclinica:
    ID = 0
    def __init__(self, nom,apaterno,amaterno,ced,fechanacimiento,edad,antecedentes,email,tel):
        hclinica.ID += 0
        self.nom = nom
        self.apellidopaterno = apaterno
        self.apellidomaterno = amaterno
        self.cedula = ced
        self.fnacimiento = fechanacimiento
        self.edad = edad
        self.correo = email
        self.telefono = tel
        self.antecedentes = antecedentes
        
    @property
    def id(self):
        return self.ID
    
    def mostrarhclinica(self):
        print(f"-"*15, "Historia Clinica", "-"*15)
        print(f"ID: ",self.id)
        print(f"Nombre: ",self.nom)
        print(f"Apellido Paterno: ",self.apellidopaterno)
        print(f"Apellido Materno: ",self.apellidomaterno)
        print(f"Cedula: ",self.cedula)
        print(f"Fecha Nacimiento: ",self.fnacimiento)
        print(f"Edad: ",self.edad)
        print(f"Correo: ",self.correo)
        print(f"Telefono: ",self.telefono)
        print(f"Antecedentes: ",self.antecedentes)
        
os.system("cls")
pac = hclinica("Anthony","Lopez","Martinez","0953758901","02/01/2003","20","Alergias, Varicela","alopezm@gmail.com","0962745197")
pac.mostrarhclinica()
