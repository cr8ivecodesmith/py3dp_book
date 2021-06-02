import openscad as o


# Create a box
o.box(20, 10, 5)  # Create a box given its XYZ dimensions
o.output(o.result(), filename='out')  # Directly create output file
