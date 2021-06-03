import openscad as o


# Create the first cone (outer)
o.cone(10, 20)
outer = o.result()

# Create the second cone (inner)
o.cone(10, 20)
o.translate(0, 0, -1)
inner = o.result()

# Make it hollow by getting the difference
o.difference([outer, inner])
hollow = o.result()


o.output(hollow, filename='out')  # Directly create output file
