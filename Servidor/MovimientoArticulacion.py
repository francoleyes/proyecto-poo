class MovimientoArticulacion():
    def __init__(self,n,a,v):
        self.articulacion=n
        self.angulo=a
        self.velocidad=v
        
    def mover(self,objeto_robot):
        objeto_robot.set_angulo_vinculo(self.articulacion,self.angulo)
    