import openscad as o


# Create and resize a sphere
o.sphere(1)
o.resize(10, 5, 2)


# Create and resize a box
o.box(1, 1, 1)
o.translate(0, 1, 0)
o.resize(10, 5, 2)


# Create, rotate, and resize a box
o.box(1, 1, 1)
o.translate(0, 2, 0)
o.rotate(0, 45, 0)
o.resize(10, 10, 2)


# Create, rotate, and resize a cylinder
o.cyl(1, 1)
o.translate(0, 8, 0)
o.rotate(0, 360, 0)
o.resize(10, 5, 3)


o.output(o.result(), filename='out')
