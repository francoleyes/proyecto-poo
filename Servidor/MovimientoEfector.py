class MovimientoEfector():
    z=0
    vel=0
    pinzas=""
    accion=0
    angulo=0
        
    def __init__(self):
        raise RuntimeError
    
    @classmethod
    def lineal(cls,z,vel):
        nueva_clase=cls.__new__(cls)
        nueva_clase.z=z
        nueva_clase.vel=vel
        return nueva_clase
    
    @classmethod
    def actividad(cls,accion,angulo):
        nueva_clase=cls.__new__(cls)
        nueva_clase.accion=accion
        nueva_clase.angulo=angulo
        return nueva_clase
    
    def mover(self,objeto_robot):
        objeto_robot.set_posicion_efector(self.z)
        
    def actividad_final(self,objeto_robot):
        if self.accion=="1":
            objeto_robot.abrir_pinzas(self.angulo)
        elif self.accion=="0":
            objeto_robot.cerrar_pinzas(self.angulo)

