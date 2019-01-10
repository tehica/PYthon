from turtle import *

wn = Screen()
ht();
def edge(kvad = Turtle(), sqt = Turtle()):
    kvad.ht(); sqt.ht();
    kvad.speed(8); sqt.speed(9)
    kvad.right(180); kvad.fd(50); kvad.right(90); kvad.fd(50);
    kvad.right(180)
    kvad.clearstamps(); kvad.clear()
    L = ["a", "a2", "a3", "4"]
    for i in range(len(L)):
        kvad.fd(100)
        kvad.left(90)
    sqt.back(50); sqt.lt(90); sqt.fd(100)
    sqt.lt(90); sqt.fd(50); sqt.clear(); sqt.lt(90)
    L2 = ['_a', '_a2', '_b', '_b2']
    for i in range(len(L2)):
        sqt.forward(200); sqt.left(90)
        
def edge2(l = Turtle()):
    l.ht();
    l.pensize(1)
    l.right(90); l.fd(70); l.rt(90); l.fd(50); l.rt(180); l.clear()
    l.fd(100); l.left(90); l.fd(4); l.back(8); l.fd(4); l.left(90)
    pomocna_kota_2_lijeva()
def edge3(N = Turtle()):
    N.ht();
    N.right(90); N.fd(120); N.right(90); N.fd(100); N.clear()
    N.back(200)
    pomocna_kota_3_lijeva()
    pomocna_kota_3_desna()
def pomocna_kota_2_lijeva(V = Turtle()):
    V.home(); V.ht();
    V.goto(-50, -70);
    V.right(90); V.forward(4); V.clear()
    V.back(8)
def pomocna_kota_3_desna(V4 = Turtle()):
    V4.home(); V4.ht();
    V4.goto(100, -120);
    V4.left(90); V4.fd(4); V4.clear()
    V4.back(8)
def pomocna_kota_3_lijeva(V3 = Turtle()):
    V3.home(); V3.ht();
    V3.goto(-100, -120);
    V3.left(90); V3.fd(4); V3.clear()
    V3.back(8)
edge(); edge2(); edge3()

s_first = Turtle(); s_scnd = Turtle()
s_first.ht();
s_first.goto(-11, -71); s_first.clear()
s_first.write(100)
s_scnd.ht();
s_scnd.goto(-11, -121); s_scnd.clear()
s_scnd.write(200)

wn.exitonclick()

