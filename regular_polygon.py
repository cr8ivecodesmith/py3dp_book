import openscad as o


# Create a pentagon
o.regular_polygon(5, 10, 3)
pentagon = o.result()


# A flat hexagon
o.regular_polygon(6, 10, o.tiny)
o.translate(25, 0, 0)
hexagon = o.result()


# A 7-sided polygon or heptagon
o.regular_polygon(7, 10, 15)
o.translate(0, 25, 0)
heptagon = o.result()


# A red "stop sign" shape is an 8-sided polygon
o.regular_polygon(8, 10, 1)
o.rgb(255, 0, 0)
o.translate(25, 25, 0)
stop_sign = o.result()


# An equilateral triangle
o.regular_polygon(3, 10, 2)
o.translate(50, 0, 0)
equi_triangle = o.result()


# A square shape from a polygon (rotated 45deg)
o.regular_polygon(4, 10, 1)
o.translate(0, 50, 0)
square = o.result()


# A circle is just another type of polygon. Though the `cyl`
# function is still the best way to do this.
o.regular_polygon(100, 10, 1)
o.translate(50, 50, 0)
circle = o.result()


# Generate the output file
o.output([
    pentagon,
    hexagon,
    heptagon,
    stop_sign,
    equi_triangle,
    square,
    circle,
], filename='out')
