class Robot:
    def __init__(self,nombre):
        self.nombre=nombre
        self.estado=0
        self.alfa1=0
        self.alfa2=0
        self.alfa3=0
        self.z_efector=0
        self.pinzas="cerradas"
        self.alfa_efector=0
        
        self.ancho=30
        self.profundidad=40
        self.alto=40
        self.vel_lineal_max=10
        self.vel_angular_max=40
    
    def activar(self):
        self.estado = 1

    def desactivar(self):
        self.estado = 0

    def set_angulo_vinculo(self,num_vinculo,angulo):
        if num_vinculo=="1":
            self.alfa1=angulo
        elif num_vinculo=="2":
            self.alfa2=angulo
        elif num_vinculo=="3":
            self.alfa3=angulo

    def set_posicion_efector(self,z): 
        self.z_efector=z
    
    def abrir_pinzas(self,angulo):
        self.pinzas="abiertas"
        self.alfa_efector=angulo

    def cerrar_pinzas(self,angulo):
        self.pinzas="cerradas"
        self.alfa_efector=angulo

    def get_reporte(self):
        cadena="""
-------------------REPORTE DE ROBOT-------------------

NOMBRE: {}
ESTADO: {}

ANGULO 1: {}
ANGULO 2: {}
ANGULO 3: {}

POSICION EFECTOR: {}
ESTADO DE PINZAS: {}
ANGULO DE PINZAS:{}
-------------------------------------------------------
        """.format(self.nombre,self.estado,self.alfa1,self.alfa2,self.alfa3,self.z_efector,self.pinzas,self.alfa_efector)
        return cadena
