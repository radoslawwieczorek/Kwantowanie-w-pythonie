import turtle

def uklad(xmax=180,ymax=180,skala=50):
   ''' rysuje żółwiem układ współrzędnych o wymiarach 2xmax * 2ymax i z jednostką skala punktów '''
   zolw = turtle.Turtle()
   zolw.speed(0)

   for i in range(2):
       zolw.fd(-xmax)
       zolw.fd(2*xmax)
       zolw.rt(135)
       zolw.fd(10)
       zolw.bk(10)
       zolw.rt(90)
       zolw.fd(10)
       zolw.bk(10)
       zolw.rt(135)
       zolw.home()
       zolw.lt(90)

   zolw.up()
   zolw.home()

   lastxtic = xmax//skala
   for x in range(-skala*lastxtic,skala*lastxtic+skala,skala):
       zolw.goto(x,0)
       zolw.down()
       zolw.write(x//skala)
       zolw.setheading(-90)
       zolw.fd(10)
       zolw.up()

   lastytic = ymax//skala
   for y in range(-skala*lastytic,skala*lastytic+skala,skala):
       zolw.goto(4,y)
       zolw.write(y//skala)
       zolw.goto(0,y)
       zolw.down()
       zolw.setheading(180)
       zolw.fd(10)
       zolw.up()

   zolw.ht()


def wektor(v, skala=50):
    ''' rysuje w zółwiowym układzie współrzędnych wektor v zaczepiony w punkcie (0,0) '''
    zolw = turtle.Turtle()
    zolw.seth(zolw.towards(v[0],v[1]))
    zolw.goto(skala*v[0],skala*v[1])


def wektor_od(v, poczatek, skala=50):
    ''' rysuje w zółwiowym układzie współrzędnych wektor v zaczepiony w punkcie poczatek '''
    zolw = turtle.Turtle()
    zolw.seth(zolw.towards(v[0],v[1]))
    zolw.up()
    zolw.goto(skala*poczatek[0],skala*poczatek[1])
    zolw.down()
    zolw.goto(skala*(poczatek[0]+v[0]),skala*(poczatek[0]+v[1]))

