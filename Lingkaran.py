import turtle

class MyTurtle:
    def __init__ (self, color, shape):
        # Membuat objek turtle
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape(shape)

    def maju(self, jarak):
        self.t.forward(jarak)

    def belok_kiri(self, sudut):
        self.t.left(sudut)

    def buat_lingkaran(self, radius):
        self.t.circle(radius)

    def selesai(self):
        turtle.done()

turtle1 = MyTurtle("purple", "turtle")
turtle1.buat_lingkaran(100)

turtle1.selesai()
