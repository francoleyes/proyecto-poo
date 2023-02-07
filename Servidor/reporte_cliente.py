def crearReporte(lista1,lista2):
    reporte=[]
    for linea in range (len(lista1)):
        reporte.append(str(lista1[linea])+"\t\t\t\t"+str(lista2[linea]))
    reporte_cadena="\n".join(reporte)
    return reporte_cadena