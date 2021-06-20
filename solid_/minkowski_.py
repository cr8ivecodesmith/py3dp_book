from solid import (
    part,
    cube,
    minkowski,
    sphere,
    cylinder,
)

from utils import render_to_openscad


def main():
    obj = part()

    obj.add(
        cube((10, 20, 3), center=False)
    )
    obj.add(
        sphere(d=5)
    )
    obj.add(
        cylinder(d=5, h=5)
    )
    obj.add(
        cube((5, 5, 5), center=False)
    )

    return minkowski()(obj)


if __name__ == '__main__':
    render_to_openscad(main(), no_run=True)
