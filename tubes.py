import openscad as o


def in_to_mm(val):
    """Inches to millimeters converter

    """
    return val * 25.4


# Create a foot-long pipe of standard 1" PVC
length = in_to_mm(12)
outside = in_to_mm(1.315)
inside = in_to_mm(1)

o.tube(outside, inside, length)


o.output(o.result(), filename='out')  # Directly create output file
