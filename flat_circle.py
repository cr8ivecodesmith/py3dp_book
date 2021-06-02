import openscad as o


# Create a flat circle
o.cyl(10, o.tiny)

f_circle = o.result()


o.output(f_circle, filename='out')  # Directly create output file
