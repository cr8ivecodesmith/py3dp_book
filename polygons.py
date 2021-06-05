import openscad as o


# Create the polygon points
p1 = [10, 0]
p2 = [-5, -5]
p3 = [-5, 30]
p4 = [15, 10]


# Create a list of these points
points = [p1, p2, p3, p4]


# Create a polygon
o.polygon(points, 2)
polygon = o.result()


o.output(polygon, filename='out')
