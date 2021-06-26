import math

from solid import (
    part,
    cylinder,
    rotate,
    cube,
    color,
    linear_extrude,
    projection,
)
from solid.utils import up, right

from utils import (
    TINY,
    render_to_openscad,
)


def projection_(obj, height: float):
    return linear_extrude(height)(
        projection()(obj)
    )


def main():

    # Example 1
    ex1 = part()

    o1_ = cylinder(d=10, h=TINY, center=False)
    o1_ = rotate((45, 0, -45))(o1_)
    o1_ = up(15)(o1_)
    ex1.add(o1_)

    o2_ = cylinder(d=10, h=TINY, center=False)
    o2_ = rotate((45, 0, -45))(o2_)
    o2_ = up(15)(o2_)
    o2_ = projection_(o2_, TINY)
    o2_ = color('red')(o2_)
    ex1.add(o2_)

    # Example 2
    ex2 = part()

    o1_ = cylinder(d=10, h=TINY, center=False)
    o1_ = rotate((45, 0, -45))(o1_)
    o1_ = up(15)(o1_)
    ex2.add(o1_)

    o2_ = cylinder(d=10, h=TINY, center=False)
    o2_ = rotate((45, 0, -45))(o2_)
    o2_ = up(15)(o2_)
    o2_ = projection_(o2_, 5)
    o2_ = color('red')(o2_)
    ex2.add(o2_)
    ex2 = right(15)(ex2)

    # Example 3
    ex3 = part()

    o1_ = cylinder(d=10, h=10, center=False)
    o1_ = rotate((45, 0, -45))(o1_)
    o1_ = up(15)(o1_)
    ex3.add(o1_)

    o2_ = cylinder(d=10, h=10, center=False)
    o2_ = rotate((45, 0, -45))(o2_)
    o2_ = up(15)(o2_)
    o2_ = projection_(o2_, 3)
    o2_ = color('red')(o2_)
    ex3.add(o2_)
    ex3 = right(35)(ex3)

    # Example 4 (Cube in a hexagon)
    ex4 = part()

    rotx = 45
    roty = math.atan(1 / math.sqrt(2)) * 180 / math.pi
    rotz = 0

    # Create a cube tilted in space
    o1_ = cube((10, 10, 10), center=False)
    o1_ = rotate(a=(roty, rotx, rotz))(o1_)
    o1_ = up(15)(o1_)
    ex4.add(o1_)

    # Also create projection of same shape
    o2_ = cube((10, 10, 10), center=False)
    o2_ = rotate(a=(roty, rotx, rotz))(o2_)
    o2_ = up(15)(o2_)
    o2_ = projection_(o2_, TINY)
    o2_ = color('red')(o2_)
    ex4.add(o2_)
    ex4 = right(45)(ex4)

    return ex1 + ex2 + ex3 + ex4


if __name__ == '__main__':
    render_to_openscad(main(), no_run=True)
