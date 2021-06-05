import openscad as o


# Create the world
o.sphere(10)
o.color('green')
earth = o.result()


# Create its moon
x = '20*sin($t*360)'
y = '20*cos($t*360)'
z = '2*cos($t*360)'
o.sphere(3)
o.rgb(32, 170, 255)
o.translate(x, y, z)
moon = o.result()


# NOTE: You will need to activate the
# View > Animate menu in OpenSCAD and adjust the FPS and Steps
# parameters to start the animation.
o.output([earth, moon], filename='out')  # Directly create output file
