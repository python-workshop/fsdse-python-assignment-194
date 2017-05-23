def sub_two(a, b):
    if a is None or b is None:
        raise TypeError('a or b cannot be None')
    result = a ^ b;
    borrow = (~a & b) << 1
    if borrow != 0:
        return sub_two(result, borrow)
    return result