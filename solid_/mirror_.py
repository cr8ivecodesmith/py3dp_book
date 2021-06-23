from solid import (
    part,
    translate,
    rotate,
    color,
    mirror,
)

from utils import render_to_openscad, text_


def main():
    ex1 = part()

    # Red text floating in space
    o_ = text_(text='Python for OpenSCAD', height=5)
    o_ = color('red')(o_)
    o_ = rotate((0, -22, 22))(o_)
    o_ = translate((15, 10, 0))(o_)
    ex1.add(o_)

    # Light-blue text mirrored in Y-Z plane
    o_ = text_(text='Python for OpenSCAD', height=5)
    o_ = color('lightblue')(o_)
    o_ = rotate((0, -22, 22))(o_)
    o_ = translate((15, 10, 0))(o_)
    o_ = mirror((1, 0, 0))(o_)
    ex1.add(o_)

    return ex1


if __name__ == '__main__':
    render_to_openscad(main(), no_run=True)
