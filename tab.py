import sys

def _measure(rows):
    lens = [0] * len(rows[0])
    for row in rows:
        for i, col in enumerate(row):
            lens[i] = len(unicode(col)) \
                      if len(unicode(col)) > lens[i] \
                      else lens[i]

    return lens

def tab(rows, spacing=1, maxw=None, fhl=sys.stdout):
    # Measure
    lens = _measure(rows)

    spc = ' ' * spacing

    # Define format
    if maxw:
        cols = ['{%d:%d.%d}' % \
                (i,
                 lth if not maxw[i] or lth < maxw[i] else maxw[i],
                 lth if not maxw[i] or lth < maxw[i] else maxw[i])
                for i, lth in enumerate(lens)]
        fmt = spc.join(cols)
    else:
        fmt = spc.join(['{%d:%d}' % (i, lth) for i, lth in enumerate(lens)])

    # Print
    for row in rows:
        print >> fhl, fmt.format(*row)
