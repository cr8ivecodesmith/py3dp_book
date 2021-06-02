import openscad as o


# A washer is just a tube!
# Create a washer for a 1/2" bolt
# Note: Dimensions found in the internet
o.tube(34.9, 14.3, 2.6)


o.output(o.result(), filename='out')  # Directly create output file
