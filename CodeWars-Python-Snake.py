def trim_canvas(canvas):
    rows = [r for r in canvas if any(c != ' ' for c in r)]
    if not rows:
        return []
    cols = list(zip(*rows))
    cols = [c for c in cols if any(ch != ' ' for ch in c)]
    return [list(r) for r in zip(*cols)]


def python_snake(body):
    positions = []
    x = y = 0
    direction = 1
    for i, length in enumerate(body):
        if i:
            y += 1
        segment = [(x + j*direction, y) for j in range(length)]
        positions.extend(segment)
        x += (length - 1)*direction
        direction *= -1
    xs, ys = zip(*positions)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    positions = [ (px - min_x, py - min_y) for px,py in positions ]
    w, h = max_x - min_x + 1, max_y - min_y + 1
    canvas = [[' ']*w for _ in range(h)]

    for idx, (px, py) in enumerate(positions):
        char = 'H' if idx==0 else ('T' if idx==len(positions)-1 else 'x')
        canvas[py][px] = char
    return canvas
