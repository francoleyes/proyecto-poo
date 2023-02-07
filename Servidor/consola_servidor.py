from cmd import Cmd
from servidor import Servidor
import os
import menu
from AccionRobot import *
import verificadorOrden

class consolaServidor(Cmd):

    doc_header = 'Ayuda de comandos documentados (escriba \'help <command>\')'
    undoc_header = 'Ayuda de comandos no documentados'
    prompt = ">> "

    def __init__(self):
        Cmd.__init__(self)
        self.rpc_server = None
        self.accion = AccionRobot()

    def do_servidor(self, value):
        '''\nInicia/Para/Muestra estado del servidor rpc según el valor dado (on/off/estado)\n'''
        if value == "on":
            if self.rpc_server is None:
                self.rpc_server = Servidor(self.accion)
            else: print('El servidor ya esta iniciado')
        elif value == "off":
            if self.rpc_server is not None:
                print("Apagando el servidor...")
                self.rpc_server.shutdown()
                self.rpc_server = None
            else: print('El servidor ya esta apagado')
        elif value=="estado": 
            if self.rpc_server is None:
                print('El servidor se encuentra apagado')
            else: print('El servidor se encuentra encendido')
        else: print('El comando "' + value + '" no esta en las opciones de servidor')

    def do_clear(self,value):
        '''\nLimpia la consola\n'''
        os.system('cls')

    def do_salir(self):
        '''\nSale del programa\n'''
        if self.rpc_server is not None:
            print("Apagando el servidor...")
            self.rpc_server.shutdown()
            self.rpc_server = None
        raise SystemExit 

    def default(self, args):
        print('\nOpción "' + args + '" no encontrada\n')

    def precmd(self, args):
        args = args.lower()
        return(args)
    
    def preloop(self):
        self.accion.inicio_robot()
        print("LADO SERVIDOR\n\nIniciando entrada de comandos...\nUtilice el comando \'help\' para obtener ayuda del sistema.")

    def do_menu(self,args):
        '''\nDespliega el menu de actividades del robot\n'''
        opcion = ''
        while opcion != "s":
            print(menu.MostrarMenu())
            opcion = input('\nEscribir comando del MENU DE COMANDOS: ').lower()
            if opcion == "a":
                print(menu.MostrarAyuda())
            elif opcion == "1":
                print(self.accion.estado_robot())
            elif opcion == "2":
                print(self.accion.actdes_robot())
            elif opcion == "r":
                print(self.accion.reporte_robot())
            elif opcion == "h":
                print(self.accion.generartxt())
            elif opcion == "c":
                if self.accion.robot.estado == 1:
                    orden = ""
                    while orden != "salir":
                        orden=verificadorOrden.verificador()
                        if orden != "salir":
                            print(self.accion.escribirGCODE(orden))
                else: 
                    print("\nPARA VER LAS ACCIONES DEL ROBOT PRIMERO TIENE QUE ACTIVAR EL ROBOT")
