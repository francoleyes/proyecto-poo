lista_ordenes=[]
mapeo = {              #Esta función sirve para reemplar el \n por nada, osea que directamente lo borra
    ord('\n'): None
}

def AbrirTxt():
     #*********************CAMBIAR POR RUTA CORRESPONDIENTE************
    archivo=open("C:/Users/DELL/Desktop/Facultad/POO/Programas/PROYECTO/Servidor/automatico.txt","r")   #abrir archivo de texto
    lista_ordenes_str=archivo.readlines()  #generar la lista que contiene que en cada componente una linea del archivo

    
    for linea in lista_ordenes_str:
        linea=linea.translate(mapeo) #borro \n de las lineas
        lista_ordenes.append(linea) # guardo la lista en otra lista

    archivo.close()
   
    return  lista_ordenes #esta lista va a contener en sus componentes una lista que es una orden

