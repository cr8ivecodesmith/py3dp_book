import openscad as o


# Create a "flat" circle
o.cyl(8, o.tiny)


# Position for rotate_extrude
o.translate(10, 4, 0)


# Flip up and spin
o.rotate_extrude()


out = o.result()
# print(out)
o.output(out, filename='out')
