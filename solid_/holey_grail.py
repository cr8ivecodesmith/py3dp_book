from solid import (
    polygon,
    sphere,

    linear_extrude,
    translate,
    rotate_extrude,
    projection,
)

from utils import TINY, CONVEXITY, render_to_openscad


def main():
    thick = 1.5
    points = (
        (0, thick),
        (10, 0),
        (10, thick),
        (thick, thick + thick),
        (thick, 20),
        (12, 30),
        (15, 45),
        (15 - thick, 45),
        (12 - thick, 31),
        (0, 21),
    )

    # Create ouline polygon
    grail = polygon(points, convexity=CONVEXITY)
    grail = linear_extrude(TINY)(grail)
    grail = projection()(grail)
    grail = rotate_extrude()(grail)

    # Make it holey
    hole_1 = sphere(d=10)
    hole_1 = translate((5, -7, 27))(hole_1)

    hole_2 = sphere(d=14)
    hole_2 = translate((-3, -10, 35))(hole_2)

    # Create the holey grail
    return grail - hole_1 - hole_2


if __name__ == '__main__':
    render_to_openscad(main(), fragments=13, debug=True)
