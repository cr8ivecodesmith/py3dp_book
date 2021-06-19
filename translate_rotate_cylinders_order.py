import openscad as o


o.cyl(1, 20)
o.rotate(45, 45, 45)
o.color('orange')

o.cyl(1, 20)
o.rotate(0, 0, 45)
o.rotate(0, 45, 0)
o.rotate(45, 0, 0)
o.color('cyan')


o.cyl(1, 20)
o.rotate(0, 0, 45)
o.color('chartreuse')


o.output(o.result(), filename='out')
