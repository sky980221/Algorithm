import sys

sys.set_int_max_str_digits(0)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        prod = 1
        count = 0
        num = n

        if n == 0:
            return 0

        else:
            for i in range(n):
                nu = num - i
                prod = prod * nu

        str_prod = str(prod)
        prod_list = []

        for i in range(len(str_prod)):
            prod_list.append(int(str_prod[i]))

        size = len(prod_list)
        prod_list.reverse()

        if size == 1:
            return count
        else:
            for i in range(size):
                if prod_list[i] != 0:
                    break
                elif prod_list[i] == 0:
                    count = count + 1
            return count