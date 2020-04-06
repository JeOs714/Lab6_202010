"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import orderedmap as map
from DataStructures import listiterator as it

import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Reto 3")
    print("1- Cargar información")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requerimiento 4")

    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    while True: 
        printMenu()
        inputs =input('Seleccione una opción para continuar\n')
        if int(inputs[0])==1:
            print("Cargando información de los archivos ....")
            print("Recursion Limit:",sys.getrecursionlimit())
            catalog = initCatalog ()
            loadData (catalog)
            print ('Arbol Accidentes cargados: ' + str(map.size(catalog['AccidentsTree'])))
            print ('Lista Accidentes cargados: ' + str(lt.size(catalog['AccidentsList'])))
            print ('Altura arbol: ' + str(map.height(catalog['AccidentsTree'])))
               
            
        elif int(inputs[0])==4:
            print("Para ingresar la fecha, el formato de la misma debe ser: Año-Mes-Día." +"\n"
            +"Por ejemplo, si desea buscar el 2 de Agosto de 2016, la entrada sería: 2016-02-08")
            date1= input("Ingrese la fecha inicio para la cual desea buscar: ")
            date2= input("Ingrese la fecha inicio para la cual desea buscar: ")
            res = controller.getRankAccidents(date1, date2, catalog)
            if res:
                print(res)
            else:
                print("No se encontraron accidentes para las fechas ", date1, " - ", date2)
        elif int(inputs[0])==2:
            print("Para ingresar la fecha, el formato de la misma debe ser: Año-Mes-Día." +"\n"
            +"Por ejemplo, si desea buscar el 2 de Agosto de 2016, la entrada sería: 2016-02-08")
            date1= input("Ingrese la fecha para la cual desea buscar los accidentes anteriores: ")
            res= controller.getAccidentBeforeDate(date1, catalog)
            if res:
                print("El número de accidentes anteriores a la fecha ingresada son", res)
            else:
                print("No se encontraron accidentes anteriores a la fecha ingresada") 

        elif int(inputs[0])==3:
            print("Para ingresar la fecha, el formato de la misma debe ser: Año-Mes-Día." +"\n"
            +"Por ejemplo, si desea buscar el 2 de Agosto de 2016, la entrada sería: 2016-02-08")
            date= input("Ingrese la fecha para la cual desea buscar las severidades: ")
            res = controller.getSeverityByDate(catalog, date)
            if res:
                print(res)
            else:
                print("No se encontraron accidentes para la fecha ",date)
        elif int(inputs[0])==5:
            print("Para ingresar la fecha, el formato de la misma debe ser: Año-Mes-Día." +"\n"
            +"Por ejemplo, si desea buscar el 2 de Agosto de 2016, la entrada sería: 2016-02-08")
            date= input("Ingrese la fecha para la cual desea buscar las severidades: ")
            res = controller.getAccidentsByState(catalog, date)
            if res:
                print(res)
            else:
                print("No se encontraron accidentes para la fecha ",date)
        elif int(inputs[0])==6:
            years = input("Ingrese los años desde y hasta (YYYY YYYY):")
            counter = controller.getBooksCountByYearRange(catalog, years) 
            if counter:
                print("Cantidad de libros entre los años",years,":",counter)
            else:
                print("No se encontraron libros para el rango de años",years)   
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    #sys.setrecursionlimit(11000)
    main()