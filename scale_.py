import openscad as o


# Create and scale a sphere
o.sphere(10)
o.scale(3, 2, 1/2)


o.output(o.result(), filename='out')
