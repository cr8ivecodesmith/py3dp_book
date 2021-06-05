import openscad as o


def prism(l, w, h):
    points = [
        [0, 0, 0],
        [l, 0, 0],
        [l, w, 0],
        [0, w, 0],
        [0, w, h],
        [l, w, h],
    ]

    faces = [
        [0, 1, 2, 3],
        [5, 4, 3, 2],
        [0, 4, 5, 1],
        [0, 3, 4],
        [5, 2, 1],
    ]

    # Create the polyhedron
    o.polyhedron(points, faces)

    # Preview unfolded polyhedron
    z = 0.08
    separation = 2
    border = .2

    o.box(l, w, z)
    o.translate(0, w+separation, 0)

    o.box(l, h, z)
    o.translate(0, w+separation+w+border, 0)

    o.box(l, (w*w+h*h)**.5, z)
    o.translate(0, w+separation+w+border+h+border, 0)

    o.triangle([0, 0], [h, 0], [0, (w*w+h*h)**.5], z)
    o.translate(l+border, w+separation+w+border+h+border, 0)

    o.triangle([0, 0], [-h, 0], [0, (w*w+h*h)**.5], z)
    o.translate(-border, w+separation+w+border+h+border, 0)


prism(10, 5, 3)


# Generate the output file
o.output(o.result(), filename='out')
