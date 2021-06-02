import openscad as o


# Create the earth
o.sphere(10)
o.color('aquamarine')
earth = o.result()


# Create its moon
o.sphere(3)
o.translate(20, 10, 10)  # move this object's xyz coords from origin
o.rgb(200, 200, 200)  # set color in rgb
moon = o.result()


# Send result to OpenSCAD
o.output([earth, moon])
