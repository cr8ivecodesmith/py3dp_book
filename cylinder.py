import openscad as o


# Create a cylinder
o.cyl(10, 20)

my_cyl = o.result()


o.output(my_cyl, filename='out')  # Directly create output file
