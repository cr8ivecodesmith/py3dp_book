from solid import (
    part,
    sphere,
    cube,
    translate,
    hull,
)
from solid.utils import right

from utils import render_to_openscad


def main():
    # -> Example 1
    ex1 = part()
    ex1.add(translate((0, 0, 0))(
        cube((5, 5, 5), center=False)
    ))
    ex1.add(translate((0, 10, 0))(
        cube((5, 5, 5), center=False)
    ))
    combo1 = hull()(ex1)

    # -> Example 2
    ex2 = part()
    ex2.add(translate((0, 0, 0))(
        cube((5, 5, 5), center=False)
    ))
    ex2.add(translate((10, 10, 0))(
        cube((5, 5, 5), center=False)
    ))
    combo2 = right(10)(
        hull()(ex2)
    )

    # -> Example 3 (Crytal-like)
    ex3 = part()
    ex3.add(translate((0, 0, 0))(
        cube((5, 5, 5), center=False)
    ))
    ex3.add(translate((10, 10, 10))(
        cube((5, 5, 5), center=False)
    ))
    combo3 = right(25)(
        hull()(ex3)
    )

    # -> Example 4 (Hot-air balloon)
    ex4 = part()
    ex4.add(sphere(d=20))
    ex4.add(translate((0, 0, -20))(
        sphere(d=3)
    ))
    combo4 = right(50)(
        hull()(ex4)
    )

    # -> Example 5 (Box with rounded corner)
    # Create 8 corner spheres
    ex5 = part()

    for x in range(-10, 20, 20):
        for y in range(-10, 20, 20):
            for z in range(-10, 20, 20):
                ex5.add(translate((x, y, z))(
                    sphere(d=10)
                ))

    combo5 = right(80)(
        hull()(ex5)
    )

    return combo1 + combo2 + combo3 + combo4 + combo5


if __name__ == '__main__':
    render_to_openscad(main(), no_run=True)
