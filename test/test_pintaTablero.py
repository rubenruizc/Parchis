from parchis.juegoParchis import Parchis


def test_pintaTablero():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 0
    parchis.fichaJ2 = 0
    
    Parchis.TAM_TABLERO = 10

    cadenaEsperada = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\n"
    cadenaEsperada += parchis.nombreJ1 + "\tI\t\t\t\t\t\t\t\t\t\tF\n"
    cadenaEsperada += parchis.nombreJ2 + "\tI\t\t\t\t\t\t\t\t\t\tF\n"

    assert parchis.pintaTablero() == cadenaEsperada

def test_pintaTablero2_1():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 2
    parchis.fichaJ2 = 1
    Parchis.TAM_TABLERO = 15

    # Cadena esperada con las posiciones correctas de los jugadores y alineación de fichas
    cadenaEsperada = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\tF\n"
    cadenaEsperada += parchis.nombreJ1 + "\tI\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    cadenaEsperada += parchis.nombreJ2 + "\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    assert parchis.pintaTablero() == cadenaEsperada


def test_pintaTablero1_1():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 1
    parchis.fichaJ2 = 1
    Parchis.TAM_TABLERO = 20

    cadenaEsperada = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    cadenaEsperada += parchis.nombreJ1 + "\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    cadenaEsperada += parchis.nombreJ2 + "\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    assert parchis.pintaTablero() == cadenaEsperada

def test_pintaTablero9_9():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 9
    parchis.fichaJ2 = 9
    Parchis.TAM_TABLERO = 10

    cadenaEsperada = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\n"
    cadenaEsperada += parchis.nombreJ1 + "\tI\t\t\t\t\t\t\t\t\tO\tF\n"
    cadenaEsperada += parchis.nombreJ2 + "\tI\t\t\t\t\t\t\t\t\tO\tF\n"

    assert parchis.pintaTablero() == cadenaEsperada

def test_pintaTablero6_3():
    parchis = Parchis("Neymar", "Messi")
    parchis.fichaJ1 = 6
    parchis.fichaJ2 = 3
    Parchis.TAM_TABLERO = 7

    cadenaEsperada = "\tI\t1\t2\t3\t4\t5\t6\tF\n"
    cadenaEsperada += parchis.nombreJ1 + "\tI\t\t\t\t\t\tO\tF\n"
    cadenaEsperada += parchis.nombreJ2 + "\tI\t\t\tO\t\t\t\tF\n"

    assert parchis.pintaTablero() == cadenaEsperada