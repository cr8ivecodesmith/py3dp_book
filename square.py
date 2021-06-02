import openscad as o


# Creates a very flat square
o.box(10, 10, o.tiny)


o.output(o.result(), filename='out')  # Directly create output file
