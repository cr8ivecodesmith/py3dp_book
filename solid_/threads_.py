from solid import (
    import_scad,
    part,
    cylinder,
    translate,
    color,
    mirror,
)
from solid.utils import right, up

from utils import (
    PROJ_DIR,
    regular_polygon,
    render_to_openscad,
)


# Import OpenScad module
# NOTE: There's a built solid.screw_thread in SolidPython module
# but the book is using this instead.
threads = import_scad(PROJ_DIR.joinpath('threads.scad').as_posix())


def right_hand_screw():
    # Threaded part
    screw_threads = threads.metric_thread(diameter=8, pitch=1, length=12)

    # Unthreaded part
    screw_solid = cylinder(d=8, h=12)
    screw_solid = translate((0, 0, -12))(screw_solid)

    # Head
    screw_head = regular_polygon(sides=6, radius=8, height=4)
    screw_head = translate((0, 0, -16))(screw_head)

    # Create the screw
    screw = screw_threads + screw_solid + screw_head

    screw = up(16)(screw)

    return screw


def main():
    screws = part()

    right_screw = right_hand_screw()
    right_screw = color('gold')(right_screw)
    right_screw = right(10)(right_screw)
    screws.add(right_screw)

    # The left-hand screw is just a mirrored version
    left_screw = right_hand_screw()
    left_screw = color('silver')(left_screw)
    left_screw = right(10)(left_screw)
    left_screw = mirror((1, 0, 0))(left_screw)
    screws.add(left_screw)

    return screws


if __name__ == '__main__':
    render_to_openscad(main(), fragments=64, no_run=True)
