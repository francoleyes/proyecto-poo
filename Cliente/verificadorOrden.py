def verifAngulo(angulo,anguloMax):

    if angulo > 0 and angulo <= anguloMax:
        
        return False
    
    else:
        print("\nElección invalida")
        return True

def verificador():

    ListaAngulosMax = (360,180,180)
    VelMaxArt = 5 #[m/s]
    
    VelMaxAct = 5 #[m/s]
    AlturaMaxActuador = 3 #[m] este valor se calcularía sumando las longitudes de las articulaciones 2 y 3
    AngMaxActuador = 80 #[°]

    flagAccion = True
    while flagAccion:
        
        print("\nSeleccionar accion: 1.Mover articulacion || 2.Mover efector || 3.Accion efector || 4.Reestablecer posicion || 5.Cargar archivo || 6.Salir")

        eleccionAccion = int(input())

        if eleccionAccion == 1:

            #Compruebo selección de articulacion
            flagArt = True
            while flagArt:
                
                print("\nSeleccionar articulacion: 1 || 2 || 3")

                eleccionArt = int(input())

                if eleccionArt == 1 or eleccionArt == 2 or eleccionArt == 3:
            
                    flagArt = False
                
                else:
                    print("\nElección inválida")

            #Compruebo selección de angulo para la articulación elegida                  
            flagAngulo = True
            while flagAngulo:
                
                print("\nSeleccionar angulo: 0-" + str(ListaAngulosMax[eleccionArt-1]))

                eleccionAng = int(input())

                flagAngulo = verifAngulo(eleccionAng , ListaAngulosMax[eleccionArt-1])

            #Compruebo que la velocidad elegida no sea mayor a la máxima
            flagVel = True
            while flagVel:    
                
                print("\nSeleccione velocidad de movimiento (m/s): 0-" + str(VelMaxArt))

                eleccionVel = int(input())

                if eleccionVel > 0 and eleccionVel <= VelMaxArt:
                    flagVel = False
                else:
                    print("\nElección inválida")

            #escribo orden
            orden = "ma:" + str(eleccionArt) + ":" + str(eleccionAng) + ":" + str(eleccionVel)

            return orden     

        elif eleccionAccion == 2:

            #Compruebo que la altura elegida sea menor a la máxima
            flagZ = True
            while flagZ:

                print("\nIngrese altura del actuador [m]: 0-" + str(AlturaMaxActuador))

                eleccionAlt = int(input())

                if eleccionAlt > 0 and eleccionAlt <= AlturaMaxActuador:
                    flagZ = False
                
                else:
                    print("\nElección invalida")
            
            #Compruebo que la velocidad no sea mayor a la máxima
            flagVel = True
            while flagVel:    
                
                print("\nSeleccione velocidad de movimiento [m/s]: 0-" + str(VelMaxAct))

                eleccionVel = int(input())

                if eleccionVel > 0 and eleccionVel <= VelMaxAct:
                    flagVel = False
                else:
                    print("\nElección inválida")

            #escribo orden
            orden = "me:" + str(eleccionAlt) + ":" + str(eleccionVel)

            return orden

        elif eleccionAccion == 3:

            #Compruebo accion del actuador
            flagPinza = True
            while flagPinza:

                print("\nAccion que realizara el actuador: 0.Cerrar || 1.Abrir")

                eleccionPinza = int (input())

                if eleccionPinza == 1 or eleccionPinza == 0:
                    flagPinza = False
                else:
                    print("\nElección invalida")

            #compruebo angulo
            flagAngPinza = True
            while flagAngPinza:

                print("\nAngulo a abrir o cerrar [°]: 0-80")

                eleccionAngPinza = int(input())

                if eleccionAngPinza >= 0 and eleccionAngPinza <= AngMaxActuador:
                    flagAngPinza = False
                else:
                    print("\nElección invalida")

            #Escribo orden
            orden = "e:" + str(eleccionPinza) + ":" + str(eleccionAngPinza)

            return orden

        elif eleccionAccion == 4:
            
            #Escribo orden
            orden = "mh"

            return orden

        elif eleccionAccion == 5:

            #Escribo orden
            orden = "mt"

            return orden

        elif eleccionAccion == 6:
            orden = "salir"
            return orden

        else:
            print("\nElección invalida")
