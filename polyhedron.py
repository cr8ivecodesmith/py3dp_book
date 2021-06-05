import openscad as o


# `points` define the coordinates of each corner.
# These are in XYZ values.
points = [
    [0, 0, 0],
    [10, 0, 0],
    [0, 15, 0],
    [0, 0, 20],
]


# `faces` define the surfaces of the polyhedron.
# 1. The number of elements in the list defines the number of surfaces.
# 2. Each element is a list whose values corresponds to the index of
#    a point in the `points` list.
# 3. The points are drawn in order which creates a plane. The right-hand
#    side is the outside of the plane.
faces = [
    [0, 3, 1],
    [1, 3, 2],
    [2, 3, 0],
    [0, 1, 2],
]


# Create the polyhedron
o.polyhedron(points, faces)


# Generate the output file
o.output(o.result(), filename='out')
