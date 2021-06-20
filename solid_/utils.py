from pathlib import Path
from subprocess import run

from solid import (
    scad_render_to_file,
    scad_render,
)


FRAGMENTS = 32  # Default
TINY = 1e-10  # Flat-ish height
CONVEXITY = 20


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
