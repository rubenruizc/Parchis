from parchis.juegoParchis import Parchis

def test_pintaTablero1():
    parchis = Parchis("Rubén","Amaro")
    
    cadenaEsperada = "I\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\n"
    
    assert parchis.pintaTablero() == cadenaEsperada