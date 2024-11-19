from parchis.juegoParchis import Parchis

def test_estadoCarrera1():
    parchis = Parchis("Amaro","Ruben")
    parchis.fichaJ1 = 5
    parchis.fichaj2 = 6

    cadenaEsperada = "El jugador 2: " + parchis.nombreJ2 + " va ganando"

    assert parchis.estadoCarrera() == cadenaEsperada

def test_estadoCarrera2():
    parchis = Parchis("Amaro","Ruben")
    parchis.fichaJ1 = 6
    parchis.fichaj2 = 5

    cadenaEsperada = "El jugador 1: " + parchis.nombreJ1 + " va ganando"

    assert parchis.estadoCarrera() == cadenaEsperada

def test_estadoCarrera3():
    parchis = Parchis("Amaro","Ruben")
    parchis.fichaJ1 = 6
    parchis.fichaj2 = 6

    cadenaEsperada = "Los jugadores 1: " + parchis.nombreJ1 + " y jugador 2: " + parchis.nombreJ2 + " van empate"

    assert parchis.estadoCarrera() == cadenaEsperada
