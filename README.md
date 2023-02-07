# Control de robot
Este es un proyecto de Programación Orientada a Objetos que permite la manipulación remota de un robot 3GDL mediante una aplicación cliente-servidor en Python utilizando un protocolo XML-RPC.

## Funcionamiento

El usuario carga en el lado cliente las órdenes por medio de la consola y el programa lo asiste para que todos los datos ingresados sean correctos. Las órdenes del cliente se envían al servidor en un formato específico, el cual las transcribe a G-Code y las envía al controlador del robot. Este controlador devuelve mensajes de estado (OK o NOK).

El diseño se realizó con un modelo de capas, lo que permite su uso independientemente de que haya una interfaz gráfica o de consola. Además, toda la entrada y salida del programa está generada en la misma capa, lo que facilita su reutilización y/o modificación.

## Más información 

Informe y videos de funcionamiento: https://drive.google.com/drive/folders/1UpU8TUyrSnyhaG4FtuhHjHHb8PPQVQI1
