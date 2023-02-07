orden_orignal=[]
orden_GCode=""

def leerOrden(orden):
    orden_orignal=orden.split(':')
    ordenGCode=escribirGCode(orden_orignal)
    return ordenGCode

def escribirGCode(lista_orden):
    if lista_orden[0]=="ma":
        orden_GCode="G 1 "+str(lista_orden[1])+" FA "+str(lista_orden[2])+" A "+str(lista_orden[3])
        return orden_GCode

    elif lista_orden[0]=="me":
        orden_GCode="G 2 "+"Z "+str(lista_orden[1])+" FL "+str(lista_orden[2])
        return orden_GCode

    elif lista_orden[0]=="mh":
        orden_GCode="G 3"
        return orden_GCode
    
    elif lista_orden[0]=="e":
        orden_GCode="G 4 "+"P "+str(lista_orden[1])+" A "+str(lista_orden[2])
        return orden_GCode

    elif lista_orden[0]=="mt":
        orden_GCode="G 5"
        return orden_GCode


