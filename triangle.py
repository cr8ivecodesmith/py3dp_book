import openscad as o

# Create a 2D triangle with a thickness of 1 unit
p1 = [0, 0]
p2 = [10, 3]
p3 = [-5, 20]

o.triangle(p1, p2, p3, 1)


o.output(o.result(), filename='out')  # Directly create output file
