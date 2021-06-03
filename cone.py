import openscad as o


# Create a cone
o.cone(10, 20)  # 10 diameter units and 20 height
cone = o.result()


o.output(cone, filename='out')  # Directly create output file
