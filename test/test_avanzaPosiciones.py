from parchis.juegoParchis import Parchis


def test_avanzaPosiciones_simple():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 3
    Parchis.dado2 = 2
    parchis.fichaJ1 = 4

    # La ficha debe avanzar 3 + 2 = 5 posiciones (4 + 5 = 9)
    posicionEsperada = 9
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == posicionEsperada


def test_avanzaPosiciones_alcanzar_limite():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 4
    Parchis.dado2 = 3
    parchis.fichaj2 = 3

    # La ficha debe avanzar 4 + 3 = 7 posiciones, alcanzando el límite (3 + 7 = 10)
    posicionEsperada = 10
    parchis.avanzaPosiciones(2)
    assert parchis.fichaj2 == posicionEsperada


def test_avanzaPosiciones_rebasar_limite():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 6
    Parchis.dado2 = 5
    parchis.fichaJ1 = 7

    # La ficha debe rebotar: 7 + (6 + 5 = 11) -> 7 + 11 = 18. Rebote: 20 - 18 = 2
    posicionEsperada = 2
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == posicionEsperada


def test_avanzaPosiciones_desde_inicio():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 2
    Parchis.dado2 = 4
    parchis.fichaj2 = 0

    # La ficha debe avanzar 2 + 4 = 6 desde la posición 0
    posicionEsperada = 6
    parchis.avanzaPosiciones(2)
    assert parchis.fichaj2 == posicionEsperada


def test_avanzaPosiciones_dos_jugadores():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 3
    Parchis.dado2 = 2
    parchis.fichaJ1 = 4
    parchis.fichaj2 = 5

    # Jugador 1 avanza 3 + 2 = 5 posiciones (4 + 5 = 9)
    posicionEsperada_J1 = 9
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == posicionEsperada_J1

    # Jugador 2 avanza 3 + 2 = 5 posiciones (5 + 5 = 10)
    posicionEsperada_J2 = 10
    parchis.avanzaPosiciones(2)
    assert parchis.fichaj2 == posicionEsperada_J2

def test_avanzaPosiciones_otroTamañoTablero():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 20
    Parchis.dado1 = 6
    Parchis.dado2 = 6
    parchis.fichaJ1 = 17

    # La ficha debe rebotar: 17 + (6 + 6 = 12) -> 17 + 12 = 29. Rebote: |20 - 29| = 11
    posicionEsperada = 11
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == posicionEsperada
