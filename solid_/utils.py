import math

from pathlib import Path
from subprocess import run

from solid import (
    # Types
    P2,

    # Operations
    union,

    # Objects
    linear_extrude,
    text,
    polygon,

    # Utils
    scad_render_to_file,
    scad_render,
)


PROJ_DIR = Path(__file__).parent.parent.absolute()  # relative to this module
FRAGMENTS = 32  # Default
TINY = 1e-10  # Flat-ish height
CONVEXITY = 20


def _cart(radius: float, angle: float):
    rad = math.radians(angle)
    x = radius * math.cos(rad)
    y = radius * math.sin(rad)
    return (x, y)


def text_(height: float = 1, *args, **kwargs):
    return linear_extrude(height)(text(*args, **kwargs))


def triangle(
    p1: P2, p2: P2, p3: P2,
    height: float,
    convexity=CONVEXITY
):
    """Triangle

    """
    return linear_extrude(height)(polygon(
        points=(p1, p2, p3), convexity=convexity
    ))


def regular_polygon(
    sides: int, radius: float, height: float
):
    """Equal sided polygons

    """
    o_ = []
    for wedge in range(sides):
        p2 = _cart(radius, wedge * 360 / sides)
        p3 = _cart(radius, (wedge + 1) * 360 / sides)
        o_.append(triangle((0, 0), p2, p3, height))
    return union()(o_)


def render_to_openscad(
    obj, fragments=FRAGMENTS, file_header=None,
    output_name=None, with_stl=False, no_run=False, debug=False
):
    file_header = file_header or ''
    if fragments and '$fn' not in file_header:
        file_header += f' $fn = {fragments};'

    if debug:
        print(scad_render(obj, file_header=file_header))

    output_name = output_name or 'out'
    output_file = Path(f'{output_name}.scad').absolute().as_posix()

    scad_render_to_file(obj, filepath=output_file, file_header=file_header)

    if not no_run:
        args = ['openscad']
        if with_stl:
            args.extend(['-o', f'{output_name}.stl'])
        args.append(output_file)
        run(args)
