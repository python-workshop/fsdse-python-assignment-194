
def sub_two(a, b):
    if a is None or b is None:
        raise TypeError('a or b cannot be None')

    if abs(a) < abs(b):
        raise ValueError("Initial number should be greater")

    result = a ^ b
    borrow = (~a & b) << 1
    if borrow != 0:
        return sub_two(result, borrow)
    return result

# print(sub_two(9,11))

"""class Solution(object):

    def sub_two(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b;
        borrow = (~a & b) << 1
        if borrow != 0:
            return self.sub_two(result, borrow)
        return result;
so = Solution()
print(so.sub_two(9,8))"""
