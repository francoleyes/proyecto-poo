from cmd import Cmd
import os
import menu
import xmlrpc.client
import verificadorOrden

class consolaCliente(Cmd):

    doc_header = 'Ayuda de comandos documentados (escriba \'help <command>\')'
    undoc_header = 'Ayuda de comandos no documentados'
    prompt = ">> "

    def __init__(self):
        Cmd.__init__(self)
        self.servidor=None

    def do_conectar(self, value):
        '''\nConecta el cliente con el servidor con ok\n'''

        if value == "ok":
            self.servidor=xmlrpc.client.ServerProxy('http://localhost:8000')
            try:
                ok=self.servidor.señalOK()
                print("CONECTADO CON SERVIDOR\n")
            except:
                print("NO SE PUEDE CONECTAR. EL SERVIDOR NO SE ENCUENTRA ENCENDIDO\n")

        else: print("\nPara conectar escriba <conectar ok>\n")

    def do_clear(self,value):
        '''\nLimpia la consola\n'''
        os.system('cls')

    def do_salir(self):
        '''\nSale del programa\n'''
        raise SystemExit 

    def default(self, args):
        print('\nOpción "' + args + '" no encontrada\n')

    def precmd(self, args):
        args = args.lower()
        return(args)
    
    def preloop(self):
        print("LADO CLIENTE\n\nIniciando entrada de comandos...\nUtilice el comando \'help\' para obtener ayuda del sistema.\n")

    def do_menu(self,args):
        '''\nDespliega el menu de actividades del robot\n'''
        try:
            ok=self.servidor.señalOK()
            opcion = ''
            while opcion != "s":
                print(menu.MostrarMenu())
                opcion = input('\nEscribir comando del MENU DE COMANDOS: ').lower()
                if opcion == "a":
                    print(menu.MostrarAyuda())
                elif opcion == "1":
                    print(self.servidor.estado_robot())
                elif opcion == "2":
                    print(self.servidor.actdes_robot())
                elif opcion == "r":
                    print(self.servidor.reporte_robot())
                elif opcion == "h":
                    print(self.servidor.generartxt())
                elif opcion == "t":

                    print("\n\n-------------------REPORTE DE TIEMPOS Y ACCIONES-------------------\n")
                    print(self.servidor.estado_robot())
                    print("\nSECUENCIA DE ACCIONES\t\tHORA DE ACCION\n")
                    print(self.servidor.reporteCliente())
                    print("\nTIEMPO ACUMULADO DESDE EL INICIO DEL ROBOT: ",self.servidor.tiempoAcumulado())

                elif opcion == "c":
                    if self.servidor.estado() == 1:
                        orden = ""
                        while orden != "salir":
                            orden=verificadorOrden.verificador()
                            if orden != "salir":
                                print(self.servidor.recibirCadena(orden))
                    else:
                        print("\nPARA VER LAS ACCIONES DEL ROBOT PRIMERO TIENE QUE ACTIVAR EL ROBOT")
        except: 
            print("\nSERVIDOR DECONECTADO. POR FAVOR CONECTELO CON <conectar ok>\n")
