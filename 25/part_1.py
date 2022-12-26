import itertools

SNAFIT_TO_DIGIT = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}

DIGIT_TO_SNAFIT = {v: k for k, v in SNAFIT_TO_DIGIT.items()}


def from_snafu(s):
    result = 0
    d = 1
    while s:
        *s, lsd = s
        result += d * SNAFIT_TO_DIGIT[lsd]
        d *= 5
    return result


def to_snafu(a):
    bases = [1]
    while sum(2 * b for b in bases) < a:
        bases.append(5 * bases[-1])
    bases.reverse()
    result = ''
    while bases:
        b, *bases = bases
        min_dist = float('inf')
        min_digit = None
        for i in [-2, -1, 0, 1, 2]:
            d = abs(a - (i * b))
            if d < min_dist:
                min_dist = d
                min_digit = i
        result += DIGIT_TO_SNAFIT[min_digit]
        a -= min_digit * b
    return result


with open('input.txt') as f:
    print(to_snafu(sum(from_snafu(line) for line in f.read().splitlines())))