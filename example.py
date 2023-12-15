import random


class Example:

    @staticmethod
    def leetcode_1277(m: int, n: int) -> list[list[int]]:
        M = []
        for i in range(m):
            q = []
            for j in range(n):
                q.append(random.randint(0, 1))

            M.append(q)
        return M