from random import *

class Parchis:
    #Clase para las funciones de parchis
    #Si son estáticos se declaran ahí
    #TODOS LOS ATRIBUTOS ANTES DEL CONSTRUCTOR SON DE CLASE ESTÁTICOS
    TAM_TABLERO = 10
    dado1 = 0
    dado2 = 0

    #Si no son estáticos se declaran ahí
    #Atributos de los objetos
    def __init__(self, nombreJ1, nombreJ2) :
        self.fichaJ1 = 0
        self.fichaj2= 0
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2
        
    #Para que un método sea estático no le pongo el self dentro, el self se utiliza para los atributos de objeto
    def tiraDados():
        Parchis.dado1 = randint(1,6)
        Parchis.dado2 = randint(1,6)
        

    
    def pintaTablero(self):
        tableroPintado = ""
        
        for i in range (Parchis.TAM_TABLERO + 1):
            if(i == 0):
                tableroPintado +="I\t"
                
            elif(i== Parchis.TAM_TABLERO):
                tableroPintado+= "F\n"
            else:
                tableroPintado += str(i) + "\t"

        return tableroPintado
    

