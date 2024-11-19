from parchis.juegoParchis import Parchis

def test_esGanador1():
    parchis = Parchis("Amaro","Ruben")
    Parchis.TAM_TABLERO = 10
    parchis.fichaJ1 = Parchis.TAM_TABLERO
    parchis.fichaj2 = 2

    mensajeEsperado = parchis.nombreJ1 +" ES EL GANADOR"

    assert parchis.esGanador() == mensajeEsperado

def test_esGanador2():
    parchis = Parchis("Amaro","Ruben")
    Parchis.TAM_TABLERO = 10
    parchis.fichaJ1 = 2
    parchis.fichaj2 = Parchis.TAM_TABLERO

    mensajeEsperado = parchis.nombreJ2 +" ES EL GANADOR"

    assert parchis.esGanador() == mensajeEsperado

def test_esGanador3():
    parchis = Parchis("Amaro","Ruben")
    Parchis.TAM_TABLERO = 10
    parchis.fichaJ1 = 2
    parchis.fichaj2 = 2

    mensajeEsperado = ""

    assert parchis.esGanador() == mensajeEsperado


def test_esGanador4():
    parchis = Parchis("Amaro","Ruben")
    Parchis.TAM_TABLERO = 20
    parchis.fichaJ1 = 20
    parchis.fichaj2 = 2

    mensajeEsperado = parchis.nombreJ1 +" ES EL GANADOR"

    assert parchis.esGanador() == mensajeEsperado


def test_esGanador5():
    parchis = Parchis("Amaro","Ruben")
    Parchis.TAM_TABLERO = 20
    parchis.fichaJ1 = 2
    parchis.fichaj2 = 20

    mensajeEsperado = parchis.nombreJ2 +" ES EL GANADOR"

    assert parchis.esGanador() == mensajeEsperado
    