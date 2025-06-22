def select(fn, iterable):
    return [item for item in iterable if fn(item)]

def reject(fn, iterable):
    return [item for item in iterable if not fn(item)]

def reduce(fn, iterable, init=None):
    if not iterable:
        return init
    result = iterable.pop() if init is None else init
    for item in iterable:
        result = fn(item, result)
    return result


def gen_reciprocals(n):
    for i in range(1, n + 1):
        yield 1 / i



def gen_capitalized(strs):
    for s in strs:
        yield s.capitalize()

def gen_selected_capitalized(strs, fn):
    for s in strs:
        if fn(s):
            yield s.capitalize()

if __name__ == '__main__':
    print(set( gen_selected_capitalized(["hello", "world"], lambda s: len(s) > 5)))

