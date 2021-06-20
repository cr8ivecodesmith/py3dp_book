import functools as ft
import operator as op

from solid import (
    cylinder,
    translate,
    rotate_extrude,
    projection,
    rotate,
)

from utils import TINY, render_to_openscad


def segment(i, spacing):
    # Create a "flat" circle
    o = cylinder(d=3, center=False, h=TINY)

    # Position for rotate extrude
    o = translate((10, spacing * i / 360, 0))(o)

    # Create 1deg slice of spiral tube
    o = projection()(o)
    o = rotate_extrude(angle=1, convexity=20)(o)

    # Rotate slice to end of spiral tube
    o = rotate((0, 0, i))(o)

    return o


def main():
    turns = 5  # Number of springs
    spacing = 5
    segs = []

    for i in range(360 * turns):
        segs.append(segment(i, spacing))

    return ft.reduce(op.add, segs)


if __name__ == '__main__':
    render_to_openscad(main(), debug=True)
