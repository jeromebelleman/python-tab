def _measure(rows):
    lens = [0] * len(rows[0])
    for row in rows:
        for i, col in enumerate(row):
            lens[i] = len(str(col)) if len(str(col)) > lens[i] else lens[i]

    return lens

def tab(rows, spacing=1, maxw=None):
    # Measure
    lens = _measure(rows)

    spc = ' ' * spacing

    # Define format
    if maxw:
        fmt = spc.join(['{%d:<%d.%d}' % (i,
                                         lth if lth < maxw else maxw,
                                         lth if lth < maxw else maxw)
                        for i, lth in enumerate(lens)])
    else:
        fmt = spc.join(['{%d:<%d}' % (i, lth) for i, lth in enumerate(lens)])

    # Print
    for row in rows:
        print fmt.format(*row)
