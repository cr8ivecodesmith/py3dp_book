import openscad as o


# Create truncated cone (top is cut off)
# Param: base diam, top face diam, height
o.cone_truncated(20, 10, 15)

o.output(o.result(), filename='out')  # Directly create output file
