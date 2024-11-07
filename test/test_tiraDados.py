
from parchis.juegoParchis import Parchis


def test_tiraDados1():
    Parchis.tiraDados()
    assert Parchis.dado1 >= 1 and Parchis.dado1 <= 6
    assert Parchis.dado2 >= 1 and Parchis.dado2 <= 6