#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      luis4god
#
# Created:     22/10/2013
# Copyright:   (c) luis4god 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    ingredientes = int (raw_input("Ingrese la cantidad de distintos ingredientes "))

    #Posibles combinaciones de pasteles ricos sin masita
    sin_masita = combinacion_sin_masita(ingredientes)

    #Posibles combinaciones de pasteles ricos con masita
    con_masita = combinacion_con_masita(ingredientes, sin_masita)

    total_pasteles_ricos = sin_masita + con_masita
    print 'La cantidad de Pasteles Ricos que se pueden formar con',\
           ingredientes,' ingredientes distintos es de',total_pasteles_ricos, \
           'Pasteles'

def combinacion_sin_masita(ingredientes):
    return 4*3**(ingredientes-2)

def combinacion_con_masita(ingredientes, sin_masita):
    return sin_masita * (ingredientes**2)

if __name__ == '__main__':
    main()
