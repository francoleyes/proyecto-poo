from xmlrpc.server import SimpleXMLRPCServer
import socket
import threading
import logging
import time

class Servidor():
    server = None
    RPC_PORT = 8000
    
    def __init__(self,accion,port = RPC_PORT):
        self.used_port = port
        self.accion=accion

        while True:
            try:
                self.server = SimpleXMLRPCServer(("localhost", self.used_port),
                                                 allow_none = True,
                                                 logRequests = None)
                if self.used_port != port:
                    logging.warning(("Servidor RPC ubicado en un puerto no estandar %d") % self.used_port)
                break
            except socket.error as e:
                if e.errno == 98:
                    self.used_port += 1
                    continue
                else:
                    print("El servidor RPC no puede ser iniciado")
                    raise

        self.server.register_function(self.do_recibirCadena, 'recibirCadena')
        self.server.register_function(self.do_señalOK, 'señalOK')
        self.server.register_function(self.do_estado_robot, 'estado_robot')
        self.server.register_function(self.do_actdes_robot, 'actdes_robot')
        self.server.register_function(self.do_reporte_robot, 'reporte_robot')
        self.server.register_function(self.do_generartxt, 'generartxt')
        self.server.register_function(self.do_estado, 'estado')
        self.server.register_function(self.do_reporteCliente, 'reporteCliente')
        self.server.register_function(self.do_tiempoAcumulado, 'tiempoAcumulado')

        self.thread=threading.Thread(target = self.run_server)
        self.thread.start()
        print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))


    def run_server(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
        self.thread.join()

    def do_recibirCadena(self,cadena):
        return self.accion.escribirGCODE(cadena)

    def do_señalOK(self):
        return "OK"

    def do_estado_robot(self):
        return self.accion.estado_robot()

    def do_actdes_robot(self):
        return self.accion.actdes_robot()
    
    def do_reporte_robot(self):
        return self.accion.reporte_robot()

    def do_generartxt(self):
        return self.accion.generartxt()

    def do_estado(self):
        return self.accion.robot.estado

    def do_reporteCliente(self):
        return self.accion.reporte_cliente()

    def do_tiempoAcumulado(self):
        return str(round(time.time()-self.accion.tiempo_inicio,2))