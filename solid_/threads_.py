from pathlib import Path

from solid import (
    import_scad,
    cylinder,
    translate,
    color,
    mirror,
)
from solid.utils import right

from utils import render_to_openscad, regular_polygon


PROJ_DIR = Path(__file__).parent.parent.absolute()

# Import OpenScad module
# NOTE: There's a built solid.screw_thread in SolidPython module
# but the book is using this instead.
threads = import_scad(PROJ_DIR.joinpath('threads.scad').as_posix())


def main():
    # Threaded part
    screw_threads = threads.metric_thread(diameter=8, pitch=1, length=12)

    # Unthreaded part
    screw_solid = cylinder(d=8, h=12)
    screw_solid = translate((0, 0, -12))(screw_solid)

    # Head
    screw_head = regular_polygon(6, 8, 4)
    screw_head = translate((0, 0, -16))(screw_head)

    # Create the screw
    screw = screw_threads + screw_solid + screw_head
    screw = color('silver')(screw)

    # Move up and away from origin
    screw = translate((10, 0, 16))(screw)

    # Mirror in the Y-Z plane
    screw = mirror((1, 0, 0))(screw)

    # Move back to origin
    screw = right(10)(screw)

    return screw


if __name__ == '__main__':
    render_to_openscad(main(), fragments=64, no_run=True)
