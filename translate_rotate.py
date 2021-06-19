import openscad as o


# Create a rectangular solid
o.box(2, 5, 9)
o.color('blue')

# Shift the position of the object
o.translate(10, 5, 0)

box1 = o.result()


# Create a rectangular solid
o.box(2, 5, 9)
o.color('red')

# Rotate around the X axis
o.rotate(45, 0, 0)

box2 = o.result()


o.output([
    box1,
    box2,
], filename='out')
