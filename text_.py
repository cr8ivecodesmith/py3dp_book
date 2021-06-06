import openscad as o

o.fragments = 100  # Smoother looking texts


# Simple text
o.text('Python for OpenSCAD', height=5)
simple_txt = o.result()


# "stamp" text
# -> Create the stamp
o.box(150, 20, 10)
o.color('chocolate')
o.translate(0, 20, 0)

# -> Place the text
o.text('Python for OpenSCAD', height=3)
o.translate(7, 26, 10)

stamp = o.result()


# Recessed text
o.box(150, 20, 10)
o.color('chocolate')
o.translate(0, 50, 0)
bg_box = o.result()

o.text('Python for OpenSCAD',
       font='Liberation Sans:style=Bold Italic',
       size=9, height=5)
o.translate(7, 56, 9)
fg_text = o.result()

o.difference([bg_box, fg_text])  # Recess the text into the box

recessed_txt = o.result()


o.output([
    simple_txt,
    stamp,
    recessed_txt,
], filename='out')
