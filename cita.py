
from doctores import paciente, personal
import os

class cita():
    def __init__(self,diagnostico, horario, sintomas, tratamientos):
        self.diagnostico = diagnostico
        self.horario = horario
        self.sintomas = sintomas
        self.tratamiento = tratamientos
        
    def mostrarcita(self):
        print(f"-"*15, "Cita Medica", "-"*15)
        print(f"Horario:",self.horario)
        print(f"Sintomas:",self.sintomas)
        print(f"Diagnostico Medico:",self.diagnostico)
        print(f"Tratamiento:",self.tratamiento)
        
if __name__ == '__main__':
    
    os.system("cls")
    medico = personal("Anthony","0953758901","alopez@gmail.com","0962745197")
    paciente = paciente("Tizi","099999999","tizi@gmail.com","099999999","Femenino","20")
    cita = cita("Falta de vitaminas","12:00 PM","Fiebre, Dolor Estomacal","Tomar cada 12 hrs 1 umbral")
    medico.mostrarusuarios()
    paciente.mostrarusuarios()
    cita.mostrarcita()
    