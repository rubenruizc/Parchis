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
                        if j == self.fichaj2:
                            tableroPintado += "O"
                    
                tableroPintado += "\tF\n"
            return tableroPintado
    
    def avanzaPosiciones(self, jugador):
        sumaDados = Parchis.dado1 + Parchis.dado2

        # Determinar cuál ficha mover
        if jugador == 1:
            ficha = self.fichaJ1
        elif jugador == 2:
            ficha = self.fichaj2

        # Calcular la posición final con rebote
        if ficha + sumaDados > Parchis.TAM_TABLERO:
            posicion = abs((Parchis.TAM_TABLERO * 2) - (ficha + sumaDados))
        else:
            posicion = ficha + sumaDados

        # Asignar la nueva posición
        if jugador == 1:
            self.fichaJ1 = posicion
        elif jugador == 2:
            self.fichaj2 = posicion


    def estadoCarrera(self):
         mensaje = ""
         if(self.fichaJ1 > self.fichaj2):
              mensaje = "El jugador 1: " + self.nombreJ1 + " va ganando"
        
         elif(self.fichaJ1 < self.fichaj2):
              mensaje = "El jugador 2: " + self.nombreJ2 + " va ganando"

         else:
              mensaje = "Los jugadores 1: " + self.nombreJ1 + " y jugador 2: " + self.nombreJ2 + " van empate"

         return mensaje;    


    def esGanador(self):
         mensajeGanador = ""

         if(self.fichaJ1 == Parchis.TAM_TABLERO):
              mensajeGanador = self.nombreJ1 +" ES EL GANADOR"
         elif(self.fichaj2 == Parchis.TAM_TABLERO):
              mensajeGanador = self.nombreJ2 +  " ES EL GANADOR"

         return mensajeGanador

