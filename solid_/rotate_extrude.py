from solid import (
    cylinder,
    translate,
    rotate_extrude,
    projection,
)

from utils import TINY, render_to_openscad


def main():
    o = cylinder(d=10, center=False, h=TINY)
    o = translate((10, 4, 0))(o)
    o = projection()(o)
    o = rotate_extrude()(o)

    return o


if __name__ == '__main__':
    render_to_openscad(main(), debug=True)
