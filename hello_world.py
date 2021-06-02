import openscad as o

# Create the world
o.fragments = 100  # Increase resolution of created objects
o.sphere(10)
earth = o.result()


# Send result to OpenSCAD
o.output(earth)
