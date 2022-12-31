from datetime import date
from titulo import titulo
from doctores import paciente
from cita import cita
import os

class Articulo:
    secuencia=0
    def __init__(self,des,pre,sto):
        Articulo.secuencia += 1
        self.descripcion = des
        self.precio = pre   
        self.stock = sto
    
    @property
    def id(self):
        return self.secuencia
        
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)

class dtreceta:
    _linea=0
    def __init__(self,articulo,cantidad):
        dtreceta._linea += 1
        self.linea = dtreceta._linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad


class receta:
    _factura = 0
    iva = 0.12
    def __init__(self,paciente,cita):
        receta._factura += 1
        self.factura = "F"+str(receta._factura)
        self.fecha = date.today()
        self.paciente = paciente
        self.cita = cita
        self.subtotal = 0
        self.iva = 0
        self.total = 0
        self.detallemedicamentos = []
        
        
    def agregardetalle(self,articulo,cantidad):
        detalle = dtreceta(articulo,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*receta.iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detallemedicamentos.append(detalle)    
    
    def mostrarreceta(self,orgnom,orgruc):
        print(f"-"*15, "Receta Medica", "-"*15)
        print("Empresa: {:12} Ruc:{}".format(orgnom,orgruc)) 
        print("Factura#:{:13} Fecha:{}".format(self.factura,self.fecha))
        self.paciente.mostrarusuarios()
        self.cita.mostrarcita()
        print("-"*50)
        print("Linea Articulo     Precio Cantidad Subtotal")
        for det in self.detallemedicamentos:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))  
        print("="*23,"Subtotal=> ",self.subtotal)
        print("="*26,"Iva=> ",self.iva)
        print("="*23,"Total=> ",self.total) 
        
os.system("cls")       
org = titulo()    
pac = paciente("Tizi","09999999","tizi@gmai.com","09999999","Femenino","21")
med = cita("Falta de victaminas","18:00 PM","Dolor de cabeza, Vomitos, Mareos","Tomar cada 12hrs 1 umbral")      
art1 = Articulo("Paracetamol",3,200)
art2 = Articulo("Aspirina",4,100)
rec = receta(pac,med)
rec.agregardetalle(art1,3)
rec.agregardetalle(art2,10)
rec.mostrarreceta(org.nombre, org.ruc)