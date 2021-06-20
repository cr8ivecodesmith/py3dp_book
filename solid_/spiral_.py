import functools as ft
import operator as op

from solid import (
    cube,
    linear_extrude,
    translate,
    projection,
    rotate,
)

from utils import CONVEXITY, FRAGMENTS, TINY, render_to_openscad


def spiral(obj, turns, height, scale=1, fragments=FRAGMENTS):
    obj = projection()(obj)
    obj = linear_extrude(
        height=height,
        twist=(360 * turns) * -1,
        scale=scale,
        slices=fragments,
        center=False,
        convexity=CONVEXITY
    )(obj)
    return obj


def main():
    spr1 = cube((10, 10, 1), center=False)
    spr1 = translate((-5, -5, 0))(spr1)
    spr1 = spiral(spr1, .25, 10)

    spr2 = cube((10, 10, 1), center=False)
    spr2 = translate((-5, -5, 0))(spr2)
    spr2 = spiral(spr2, .25, 10, 0)
    spr2 = translate((15, 0, 0))(spr2)

    spr3 = cube((10, 10, 1), center=False)
    spr3 = translate((-5, -5, 0))(spr3)
    spr3 = spiral(spr3, -.5, 10, .5, 80)
    spr3 = translate((0, 15, 0))(spr3)

    # A spiral ramp
    spr4 = cube((20, 1, TINY), center=False)
    spr4 = translate((2, 0, 0))(spr4)
    spr4 = spiral(spr4, 1, 30)
    spr4 = translate((0, -45, 0))(spr4)

    # A spiral stacked cubes
    stack = []
    for i in range(30):
        o_ = cube((20, 5, 1), center=False)
        o_ = translate((2, 0, 0))(o_)
        o_ = rotate((0, 0, 360 * i / 30))(o_)
        o_ = translate((0, 0, i))(o_)
        stack.append(o_)
    spr_stack = ft.reduce(op.add, stack)
    spr_stack = translate((-45, 0, 0))(spr_stack)

    return spr1 + spr2 + spr3 + spr4 + spr_stack


if __name__ == '__main__':
    render_to_openscad(main(), debug=True)
