"""Alternative code for color.py where the
commands are buffered in single string.

"""
import openscad as o


# Create the earth
o.sphere(10)
o.color('aquamarine')

# Create its moon
o.sphere(3)
o.translate(20, 10, 10)  # move this object's xyz coords from origin
o.rgb(200, 200, 200)  # set color in rgb


# Finalize the commands
earth_and_moon = o.result()


# Send result to OpenSCAD
o.output(earth_and_moon)
