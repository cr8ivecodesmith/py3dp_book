import openscad as o

# Create first flattish, red circle
o.cyl(15, o.tiny)
o.color('red')
disk1 = o.result()

# Rotate second blue circle around Y
o.cyl(12, o.tiny)
o.rotate(0, 90, 0)
o.color('blue')
disk2 = o.result()

# Rotate green circle around X
o.cyl(9, o.tiny)
o.rotate(90, 0, 0)
o.color('green')
disk3 = o.result()

# Rotate yellow circle around X, then Y, then X
o.cyl(17, o.tiny)
o.rotate(45, 10, -135)
o.color('yellow')
disk4 = o.result()

# Create a modifiable single object
o.union([disk1, disk2, disk3, disk4])

# Translate the whole construct
o.translate(15, 10, 5)

o.output(o.result(), filename='out')
