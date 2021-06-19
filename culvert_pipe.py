import openscad as o


# Create a tube
o.tube(10, 9.8, 20)
o.scale(2, 1, 1)


o.output(o.result(), filename='out')
