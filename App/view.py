"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
# ___________________________________________________
#  Variables
# ___________________________________________________
import controller

servicefile = '201801-1-citibike-tripdata.csv'
initialStation = None
recursionLimit = 20000

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar datos de Citibike")
    print("3- REQUERIMIENTO 1")
    print("4- REQUERIMIENTO 2")
    print("5- REQUERIMIENTO 3")
    print("6- REQUERIMIENTO 4")
    print("7- REQUERIMIENTO 5")
    print("8- REQUERIMIENTO 6")
    print("0- Salir")
    print("*******************************************")


def CargarDatos(): #CARGAR INFORMACION
    print("\nCargando información de transporte de singapur ....")
    # para todos los archivos
    #controller.loadTrips(cont)
    # para uno solo
    controller.loadFile(cont, servicefile)
    numedges = controller.totalConnections(cont)
    numvertex = controller.totalVertex(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print('El limite de recursion se ajusta a: ' + str(recursionLimit))

def Requerimiento1():
    Station1= input("Ingrese una estacion de interés: ")
    Station2= input("Ingrese otra estacion de interés: ")
    print('El número de componentes conectados es: ' + 
            str(controller.numSCC(cont)))
    print("Entre "+str(Station1)+" y "+str(Station2)+": "+
            str(controller.sameCC(cont,Station1,Station2))+ "que pertenezcan al mismo cluster")

def Requerimiento2():
    tiempoInicial= input("Ingrese su tiempo incial disponible para un viaje: ")
    tiempoFinal= input("Ingrese su tiempo final disponible para un viaje: ")
    id_salida= input("Ingrese el id de la estacion de partida: ")
    i=0
    respuesta= controller.RutasCirculares(cont, id_salida, tiempoInicial, tiempoFinal)
    
    iter=it.newIterator(respuesta)
    i=0
    print("Ruta #"+"\t"+"\t"+"NOMBRE ESTACION"+"\t"+"\t"+"DURACION")
    print("-------------------------------------------------------")
    while it.hasNext(iter):
        ruta_circular= it.next(iter)
        cantidad_rutas=lt.size(ruta_circular) 
        iter2=it.newIterator(ruta_circular)
        while it.hasNext(iter2):
            informacion= it.next(iter2)
            
            P
            duracion= informacion['duracion']
            print(str(i)+"\t"+"\t"+ nombre+"\t"+"\t"+str(duracion))
            
            # nombre=informacion['estacion1']]['value']
            # print(nombre)
            i+=1
    print("Rutas Circulares encontradas: "+ str(cantidad_rutas))

    # imprimirReq2(respuesta[0], respuesta[1], tiempoInicial, tiempoFinal)

def imprimirReq2(pesoTotal, vertices, tiempoInicial, tiempoFinal):
    i=0
    if peso>int(tiempoInicial) and peso<int(tiempoFinal):
        print("Estacion de salida: "+ vertices[0])
        print("Estacion de llegada: "+ vertices[1])
        i+=1
    else:
        print("No hay rutas circulares")
    print("Total de rutas circulaes: "+ str(i))
    print("Tiempo total del recorrido: "+ str(peso))

    
# def Requerimiento3():

# def Requerimiento4():

# def Requerimiento5():

def Requerimiento6():
   
    lat1 = float(input("Inserte la latitud de salida: "))
    lon1 = float(input("Inserte la longitud de salida: "))
    lat2 = float(input("Inserte la latitud de llegada: "))
    lon2 = float(input("Inserte la longitud de llegada: "))
    res = controller.RutaInteresTuristico(cont, lat1, lon1, lat2, lon2)
    
    print("La estación más cercana a la posición {0}, {1} (salida) es: {2}".format(lat1,lon1,res[0]))
    print("La estación más cercana a la posición {0}, {1} (llegada) es: {2}".format(lat2,lon2,res[1]))
    if res[2] != None:
        print("La ruta más corta desde la estación {0} hasta la estación {1} es {2}.\nEsta ruta tiene una duración de {3}.".format(res[0],res[1],res[2],res[3]))
    else:
        print("No existe una ruta entre estas dos estaciones.")
    



"""
Menu principal
"""
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(CargarDatos, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 3:
        executiontime = timeit.timeit(Requerimiento1, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 4:
        executiontime = timeit.timeit(Requerimiento2, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 5:
        executiontime = timeit.timeit(Requerimiento3, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 6:
        executiontime = timeit.timeit(Requerimiento4, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 7:
        executiontime = timeit.timeit(Requerimiento5, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 8:
        executiontime = timeit.timeit(Requerimiento6, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    else:
        sys.exit(0)
sys.exit(0)


