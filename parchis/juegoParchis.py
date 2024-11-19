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

            for i in range(1, 4):
                if i == 2:
                    tableroPintado += self.nombreJ1
                elif i == 3:
                    tableroPintado += self.nombreJ2
                
                tableroPintado += "\tI"

                for j in range(1, Parchis.TAM_TABLERO):
                    tableroPintado += "\t"

                    if i == 1:
                        tableroPintado += str(j)
                    elif i == 2:
                        if j == self.fichaJ1:
                            tableroPintado += "O"
                    elif i == 3:
                        if j == self.fichaJ2:
                            tableroPintado += "O"
                    
                tableroPintado += "\tF\n"
            return tableroPintado
    
    #Un método no puede ser estatico si voy a modificar un atributo dentro
    def avanzaPosiciones(self,ficha,jugador):
            sumaDados = (Parchis.dado1 + Parchis.dado2)
        
        # Por defecto, le damos el valor de sumaDados
            posicion = sumaDados

        # Si la suma de la posición actual más la suma de los dados es mayor que el tablero, usamos la fórmula para el rebote
            if (ficha + sumaDados > Parchis.TAM_TABLERO):
            # Caso práctico
            # TAM -> 10
            # Jugador en 6
            # Suma dados -> 8
            # 20 - 14 (6+8) = 6, esta es la posición final
            # Usamos absoluto para los negativos
                posicion = abs((Parchis.TAM_TABLERO * 2) - (ficha + sumaDados))

            if(jugador == 1):
                 self.fichaJ1 = posicion
            elif(jugador == 2):
                 self.fichaj2 = posicion


