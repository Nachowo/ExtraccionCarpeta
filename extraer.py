import os
#import zipfile
import shutil



#funcion para extraer todos los archivos .pl de un conjunto de carpetas
def extraer(directorio,destino):
    actual = directorio
    #recorre todos los archivos en el directorio actual
    for x in os.listdir(actual):
        archivo = actual+'/'+x
        #si el archivo actual es una carpeta, si es así hace la llamada recursiva
        if(os.path.isdir(archivo)):
            extraer(archivo,destino)
        #Si es un archivo revisa que no sea de pruebas y sea un .pl
        else:
            if(x.endswith('.pl') and (not "prueba" in x.lower())):
                #Copia de archivo protegida
                try:
                    shutil.copy(archivo,destino+'/'+x)
                except shutil.SameFileError:
                    print("\n el archivo ya esta")
                except:
                    print("\nfallo al copiar: "+x)

#Bloque main
__name__="__main__"

#El destino es una carpeta en especifico
destino = 'C:/Users/arias/OneDrive/Escritorio/Labs prolog/FINAL'

#Verifica que exista el directorio de destino
try:
    os.mkdir(destino)
except FileExistsError:
    print("ya existe el archivo")

#Realiza la operación
extraer('C:/Users/arias/OneDrive/Escritorio/Labs prolog',destino)

