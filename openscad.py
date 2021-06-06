import math
import inspect


__all__ = [
    'startup',
    'literally',
    'cyl',
    'cylinder',
    'cone',
    'cone_truncated',
    'sphere',
    'box',
    'polygon',
    'triangle',
    'regular_polygon',
    'tube',
    'polyhedron',
    'text',
    'translate',
    'rotate',
    'scale',
    'resize',
    'mirror',
    'color',
    'rgb',
    'offset_round',
    'offset_straight',
    'offset_chamfer',
    'projection',
    'slice',
    'spiral',
    'rotate_extrude',
    'union',
    'difference',
    'intersection',
    'hull',
    'minkowski',
    'surface',
    'result',
    'output',
    'platonic_cube',
    'platonic_tetrahedron',
]


# Global commands accumulator
_cmds = ""
_use = ""

# Function modifying parameters
fragments = 31

# Constants
tiny = 1e-99


# Functions for driving Openscad


def startup(s):
    global _use
    _use += f"""{s}\n"""


def literally(s):
    global _cmds
    _cmds += f"""{s}\n"""


def cyl(diameter, height):
    """Creates a cylinder givent the diameter and height.

    """
    global _cmds, fragments
    radius = diameter / 2
    _cmds = (
        f"cylinder(h={height},"
        f"r1={radius},r2={radius},"
        f"center=false,$fn={fragments});\n\n"
        ) + _cmds


def cylinder(diameter, height):
    global _cmds, fragments
    radius = diameter / 2
    _cmds = (
        f"cylinder(h={height},"
        f"r1={radius},r2={radius},"
        f"center=false,$fn={fragments});\n\n"
        ) + _cmds


def cone(diameter, height):
    global _cmds, fragments
    radius = diameter / 2
    _cmds = (
        f"cylinder(h={height},"
        f"r1={radius},r2={0},"
        f"center=false,"
        f"$fn={fragments});\n\n"
        ) + _cmds


def cone_truncated(diameter1, diameter2, height):
    global _cmds, fragments
    radius = diameter1 / 2
    radius2 = diameter2 / 2
    _cmds = (
        f"cylinder(h={height},r1={radius},"
        f"r2={radius2},center=false,"
        f"$fn={fragments});\n\n"
    ) + _cmds


def sphere(diameter):
    global _cmds, fragments
    radius = diameter / 2
    _cmds = (f"sphere({radius},"
             f"$fn={fragments});\n\n") + _cmds


def box(x, y, z):
    """Create a box given the XYZ dimensions

    """
    global _cmds
    _cmds = (f"cube({[x,y,z]},"
             f"center=false);\n\n") + _cmds


def polygon(points_list, height):
    global _cmds, fragments
    _cmds = (
        f"linear_extrude({height})\n"
        f"polygon({points_list},"
        f"convexity=20,$fn={fragments});\n\n"
        ) + _cmds


def triangle(point1, point2, point3, height):
    polygon([point1, point2, point3], height)


def regular_polygon(sides, radius, height):
    """Regular polygons have equal sides and interior angles

    ::NOTES::
    Radius starts from origin.

    """
    global _cmds
    _cmds = "}\n\n" + _cmds
    for wedge in range(sides):
        p1 = _cart(radius, wedge*360/sides)
        p2 = _cart(radius, (wedge+1)*360/sides)
        triangle([0, 0], p1, p2, height)
    _cmds = "union(){\n" + _cmds


def tube(outside_diam, inside_diam, height):
    """Creates a tube given the outside and inside diameters

    """
    global _cmds, fragments
    r1 = outside_diam / 2
    r2 = inside_diam / 2
    _cmds = (
        "difference(){\n"
        f"cylinder(h={height},r1={r1},r2={r1},"
        f"center=false,$fn={fragments});\n"
        f"cylinder(h={height*3},r1={r2},r2={r2},"
        f"center=true,$fn={fragments});\n"
        "}\n") + _cmds


def polyhedron(points_list, faces_list):
    global _cmds
    _cmds = (f"polyhedron({points_list},"
             f"{faces_list},convexity=20);\n\n") + _cmds


def text(
    text="",
    size=10,
    font="Liberation Sans",
    halign="left",
    valign="baseline",
    spacing=1,
    direction="ltr",
    language="en",
    script="latin",
    height=1,
):
    global _cmds, fragments
    _cmds = (
        f'linear_extrude({height})\n'
        f'text(text="{text}",size={size},'
        f'font="{font}",halign="{halign}",'
        f'valign="{valign}",spacing={spacing},'
        f'direction="{direction}",'
        f'language="{language}",'
        f'script="{script}",'
        f'$fn={fragments});\n\n'
    ) + _cmds


def translate(x, y, z):
    """Move the object's XYZ coords from origin

    """
    global _cmds
    _cmds = f"translate([{x},{y},{z}])\n" + _cmds


def rotate(x, y, z):
    global _cmds
    _cmds = f"rotate([{x},{y},{z}])\n" + _cmds


def scale(x, y, z):
    global _cmds
    _cmds = f"scale([{x},{y},{z}])\n" + _cmds


def resize(x, y, z):
    global _cmds
    _cmds = f"resize([{x},{y},{z}])\n" + _cmds


def mirror(x, y, z):
    global _cmds
    _cmds = f"mirror([{x},{y},{z}])\n" + _cmds


def color(color_name, alpha=1.0):
    """Set color of object based on name.

    """
    global _cmds
    _cmds = (f'color("{color_name}",'
             f'{alpha})\n') + _cmds


def rgb(r, g, b, alpha=1.0):
    """Set color of object based on RGB values.

    """
    global _cmds
    _cmds = (f"color([{r/255},{g/255},"
             f"{b/255},{alpha}])\n") + _cmds


def offset_round(distance, height):
    global _cmds, fragments
    _cmds = (
        f"linear_extrude({height})\n"
        f"offset(r={distance},chamfer=false,"
        f"$fn={fragments})\n"
        f"projection()\n") + _cmds


def offset_straight(distance, height):
    global _cmds
    _cmds = (
        f"linear_extrude({height})\n"
        f"offset(delta={distance},"
        f"chamfer=false)\n"
        f"projection()\n"
        ) + _cmds


def offset_chamfer(distance, height):
    global _cmds
    _cmds = (
        f"linear_extrude({height})\n"
        f"offset(delta={distance},"
        f"chamfer=true)\n"
        f"projection()\n"
        ) + _cmds


def projection(height):
    global _cmds
    _cmds = (f"linear_extrude({height})"
             f"\nprojection()\n") + _cmds


def slice(height):
    global _cmds
    _cmds = (f"linear_extrude({height})\n"
             f"projection(cut=true)\n") + _cmds


def spiral(turns, height, scale=1):
    global _cmds, fragments
    _cmds = (
        f"linear_extrude(height={height},"
        f"twist=-{360*turns},"
        f"scale={scale},"
        f"slices={fragments},"
        f"center=false,"
        f"convexity=20,"
        f"$fn={fragments})\n"
        f"projection()\n"
    ) + _cmds


def rotate_extrude(angle=360):
    global _cmds, fragments
    _cmds = (
        f"rotate_extrude(angle={angle},"
        f"convexity=20,$fn={fragments})\n"
        f"projection()\n"
    ) + _cmds


def union(obj_list):
    global _cmds
    cmd = "union(){\n"
    for obj in obj_list:
        cmd += obj
    cmd += "}\n"
    _cmds = cmd + _cmds


def difference(obj_list):
    global _cmds
    cmd = "difference(){\n"
    for obj in obj_list:
        cmd += obj
    cmd += "}\n"
    _cmds = cmd + _cmds


def intersection(obj_list):
    global _cmds
    cmd = "intersection(){\n"
    for obj in obj_list:
        cmd += obj
    cmd += "}\n"
    _cmds = cmd + _cmds


def hull(obj_list):
    global _cmds
    cmd = "hull(){\n"
    for obj in obj_list:
        cmd += obj
    cmd += "}\n"
    _cmds = cmd + _cmds


def minkowski(obj_list):
    global _cmds
    cmd = "minkowski(){\n"
    for obj in obj_list:
        cmd += obj
    cmd += "}\n"
    _cmds = cmd + _cmds


def surface(filename, invert="false"):
    global _cmds
    _cmds = (f'surface(file=\"{filename}\",'
             f'convexity=5,'
             f'invert={invert});\n') + _cmds


def result():
    """Return generated OpenSCAD command string and clear the buffer.

    """
    global _cmds
    res = _cmds
    _cmds = ""
    return res


def output(cmds_list="", filename=None):
    """Generate the OpenSCAD script from the given command string or list.

    """
    global _use
    calling_file = inspect.stack()[1].filename
    srcfile = calling_file.split("\\")[-1]

    dstfile = (
        f'{filename}.scad' if filename else srcfile.replace(".py", ".scad")
    )

    f = open(dstfile, "w")
    if _use:
        f.write(_use)
        _use = ""
    for cmd in cmds_list:
        f.write(cmd)
    f.close()


def platonic_cube(n):
    box(n, n, n)
    translate(-n / 2, -n / 2, -n / 2)


def platonic_tetrahedron(n):
    n0 = n * (8 / 3) ** -0.5
    n1 = ((8 / 9) ** 0.5) * n0
    n2 = ((2 / 9) ** 0.5) * n0
    n3 = ((2 / 3) ** 0.5) * n0
    n4 = -n0 / 3
    v0 = [n1, 0, n4]
    v1 = [-n2, n3, n4]
    v2 = [-n2, -n3, n4]
    v3 = [0, 0, n0]
    points = [v0, v1, v2, v3]
    faces = [[0, 1, 2], [0, 3, 1],
             [1, 3, 2], [2, 3, 0]]
    polyhedron(points, faces)


def platonic_octahedron(n):
    n0 = n * 2 ** -0.5
    v0 = [n0, 0, 0]
    v1 = [-n0, 0, 0]
    v2 = [0, n0, 0]
    v3 = [0, -n0, 0]
    v4 = [0, 0, n0]
    v5 = [0, 0, -n0]
    points = [v0, v1, v2, v3, v4, v5]
    faces = [
        [0, 4, 2],
        [2, 4, 1],
        [1, 4, 3],
        [3, 4, 0],
        [2, 5, 0],
        [1, 5, 2],
        [3, 5, 1],
        [0, 5, 3],
    ]
    polyhedron(points, faces)


def platonic_dodecahedron(n):
    phi = (1 + 5 ** 0.5) / 2
    fac = n * phi / 2
    n0 = phi * fac
    n1 = fac / phi
    v0 = [fac, fac, fac]
    v1 = [-fac, fac, fac]
    v2 = [fac, -fac, fac]
    v3 = [-fac, -fac, fac]
    v4 = [fac, fac, -fac]
    v5 = [-fac, fac, -fac]
    v6 = [fac, -fac, -fac]
    v7 = [-fac, -fac, -fac]
    v8 = [0, n0, n1]
    v9 = [0, -n0, n1]
    v10 = [0, n0, -n1]
    v11 = [0, -n0, -n1]
    v12 = [n1, 0, n0]
    v13 = [n1, 0, -n0]
    v14 = [-n1, 0, n0]
    v15 = [-n1, 0, -n0]
    v16 = [n0, n1, 0]
    v17 = [-n0, n1, 0]
    v18 = [n0, -n1, 0]
    v19 = [-n0, -n1, 0]
    points = [
        v0,
        v1,
        v2,
        v3,
        v4,
        v5,
        v6,
        v7,
        v8,
        v9,
        v10,
        v11,
        v12,
        v13,
        v14,
        v15,
        v16,
        v17,
        v18,
        v19,
    ]
    f1 = [0, 16, 18, 2, 12]
    f2 = [14, 12, 2, 9, 3]
    f3 = [19, 3, 9, 11, 7]
    f4 = [15, 7, 11, 6, 13]
    f5 = [4, 13, 6, 18, 16]
    f6 = [2, 18, 6, 11, 9]
    f7 = [12, 14, 1, 8, 0]
    f8 = [3, 19, 17, 1, 14]
    f9 = [7, 15, 5, 17, 19]
    f10 = [13, 4, 10, 5, 15]
    f11 = [16, 0, 8, 10, 4]
    f12 = [1, 17, 5, 10, 8]
    faces = [f1, f2, f3, f4, f5, f6,
             f7, f8, f9, f10, f11, f12]
    polyhedron(points, faces)


def platonic_icosahedron(n):
    phi = (1 + 5 ** 0.5) / 2
    fac = n / 2
    n0 = phi * fac
    v0 = [0, fac, n0]
    v1 = [0, fac, -n0]
    v2 = [0, -fac, n0]
    v3 = [0, -fac, -n0]
    v4 = [fac, n0, 0]
    v5 = [fac, -n0, 0]
    v6 = [-fac, n0, 0]
    v7 = [-fac, -n0, 0]
    v8 = [n0, 0, fac]
    v9 = [-n0, 0, fac]
    v10 = [n0, 0, -fac]
    v11 = [-n0, 0, -fac]
    points = [v0, v1, v2, v3, v4, v5, v6,
              v7, v8, v9, v10, v11]
    f1 = [2, 9, 0]
    f2 = [2, 7, 9]
    f3 = [2, 5, 7]
    f4 = [2, 8, 5]
    f5 = [2, 0, 8]
    f6 = [1, 4, 6]
    f7 = [1, 6, 11]
    f8 = [1, 11, 3]
    f9 = [1, 3, 10]
    f10 = [1, 10, 4]
    f11 = [0, 6, 4]
    f12 = [6, 0, 9]
    f13 = [9, 11, 6]
    f14 = [11, 9, 7]
    f15 = [7, 3, 11]
    f16 = [3, 7, 5]
    f17 = [5, 10, 3]
    f18 = [10, 8, 5]
    f19 = [8, 4, 10]
    f20 = [4, 8, 0]
    faces = [
        f1,
        f2,
        f3,
        f4,
        f5,
        f6,
        f7,
        f8,
        f9,
        f10,
        f11,
        f12,
        f13,
        f14,
        f15,
        f16,
        f17,
        f18,
        f19,
        f20,
    ]
    polyhedron(points, faces)


# Local utility functions

def _cart(radius, angle):
    rad = math.radians(angle)
    x = radius * math.cos(rad)
    y = radius * math.sin(rad)
    return [x, y]
