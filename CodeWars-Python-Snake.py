from itertools import accumulate

def python_snake(xs):
    w = list(accumulate(x * (-1)**i for i, x in enumerate(xs)))
    mi, ma = min(w), max(w)
    n = mi < 0 and ma - mi or max(w[-1], ma)
    H = start = max(0, -mi)
    result = [list(' ' * n) for _ in xs]
    for i, x in enumerate(xs):
        end = start + x * (-1)**i
        result[i][slice(*sorted([start, end]))] = 'x' * x
        start = end
    result[0][H] = 'H'
    result[-1][end - (len(xs) & 1)] = 'T'
    return result
