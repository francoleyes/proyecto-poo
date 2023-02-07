from datetime import datetime
import time
from Robot import *
from AccionRobot import *
from MovimientoArticulacion import *
from MovimientoEfector import *
from MovimientoOrigen import *
import conversorGCode
import LeerArchivoTexto
import reporte_cliente

class AccionRobot:
    def __init__(self):
        self.robot=Robot("Robert")
        self.lista_ordenes_totales=[]
        self.lista_tiempo = []
        self.tiempo_inicio=0
    
    def desplazamiento(self,objeto_accion):              
        objeto_accion.mover(self.robot) 
    
    def trabajo_efector(self,objeto_accion):
        objeto_accion.actividad_final(self.robot)

    def estado_robot(self):
        if self.robot.estado==1:
            return "\nESTADO DEL ROBOT: ACTIVADO"
        elif self.robot.estado==0:
            return "\nESTADO DEL ROBOT: DESACTIVADO"

    def actdes_robot(self):
        if self.robot.estado==0:
            self.robot.activar()
            return "\nROBOT ACTIVADO"
        elif self.robot.estado==1:
            self.robot.desactivar()
            return "\nROBOT DESACTIVADO"

    def reporte_robot(self):
        return self.robot.get_reporte()

    def interprete_comandos(self,orden):
        orden_original=orden.split(' ')
        
        if orden_original[1]=="1":
            obj=MovimientoArticulacion(orden_original[2],orden_original[4],orden_original[6])
            self.desplazamiento(obj)
                         
        elif orden_original[1]=="2":
            obj=MovimientoEfector.lineal(orden_original[3],orden_original[5])
            self.desplazamiento(obj)
            
        elif orden_original[1]=="3":    
            obj=MovimientoOrigen()
            self.desplazamiento(obj)

        elif orden_original[1]=="4": 
            obj=MovimientoEfector.actividad(orden_original[3],orden_original[5])
            self.trabajo_efector(obj)

        elif orden_original[1]=="5":
            lista_ordenes=LeerArchivoTexto.AbrirTxt()
            for lista in lista_ordenes:
                self.escribirGCODE(lista)

    def generartxt(self):
        archivo=open("datos.txt","w") 
        for orden in self.lista_ordenes_totales:
            archivo.write(str(orden)+"\n") 
        archivo.close()
        return "\nARCHIVO GENERADO"

    def escribirGCODE(self,cadena):
        if self.robot.estado == 1:
            cGCODE=conversorGCode.leerOrden(cadena)
            self.interprete_comandos(cGCODE)

            hora = str(datetime.now())
            self.lista_ordenes_totales.append(cadena)
            self.lista_tiempo.append(hora)

            return "\nORDEN ENVIADA"
        elif self.robot.estado == 0:
            return "\nNO PUEDE EJECUTAR COMANDOS YA QUE EL ROBOT ESTA DESACTIVADO"

    def reporte_cliente(self):
        return reporte_cliente.crearReporte(self.lista_ordenes_totales,self.lista_tiempo)
    
    def inicio_robot(self):
        self.tiempo_inicio=time.time()