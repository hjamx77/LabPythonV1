#esta versión se subirá a git hub
import random
import math
#from re import I

def valida_rangos(numero2):
#Evalua que el número que ingresó se encuentre dentro del rango determinado
    numero2=float(numero2)
    numero2=math.trunc(numero2)   
    numero2=int(numero2)
    if numero2 < 1 or numero2 >10:
        while (numero2 <= 1 or numero2 >= 10):
            print ('Recuerda solo se deben ingresar números del 1 al 10')
            numero2=input('Vuelve a teclear el número que crees que pensé: ')
            numero2=float(numero2)
            numero2=math.trunc(numero2)   
            numero2=int(numero2)
    else:
        return numero2


def adivinanum():
#Evalua que el número que ingresó sea adivinado en 5 oportunidades

    INTENTOS=5
    numero=random.randrange(1,10)
    numero=int(numero)
    numero2=input('Teclea el número que crees que pensé: ')
    numero2=float(numero2)
    numero2=math.trunc(numero2)   
    numero2=int(numero2)
    #print(numero)
    #print(numero2)
    numero2=valida_rangos(numero2)

    i=1
    while i <= INTENTOS:
        #print ('Entro al bucle con la oportunidad: ' + str(i) )
        
        if numero==numero2:
            print('Felicidades adivinaste el número que pensé!!!, en el intento:' + str(i))
            return True
            break
        elif numero != numero2:            
            restante= (INTENTOS - i)
            print ('Fallaste, es tu ' + str(i) + ' oportunidad, te sobran ' + str(restante) + ' oportunidades' )
            i = i + 1
            if i == 6:
                print(' :( El número que pensé fue el ' + str(numero))
                break
            numero2=input('Teclea el número que crees que pensé: ')
            numero2=valida_rangos(numero2)
    return False

def run():
    print('Piensa un número dentro del rango del 1 al 10 tienes 5 oportunidades (el programa no considera decimales)')
    resultado=adivinanum()
    if resultado==False:
        print('No adivinaste el número, suerte para la próxima')


if __name__ == '__main__':
    run()