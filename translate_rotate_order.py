import openscad as o


# Rotate then translate
o.box(2, 5, 9)
o.color('blue')
o.rotate(0, 0, 90)
o.translate(10, 0, 0)

box1 = o.result()


# Translate then rotate
o.box(2, 5, 9)
o.color('red')
o.translate(10, 0, 0)
o.rotate(0, 0, 90)

box2 = o.result()


o.output([
    box1,
    box2,
], filename='out')
