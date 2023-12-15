import random


class Example:

    @staticmethod
    def leetcode_1277(m: int | None = None, n: int | None = None) -> list[list[int]]:
        if m and n:
            pass
        else:
            m = random.randint(1, 4)
            n = random.randint(1, 4)
        M = []
        for i in range(m):
            q = []
            for j in range(n):
                q.append(random.randint(0, 1))

            M.append(q)
        return M