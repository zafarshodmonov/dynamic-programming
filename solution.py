class Solution:

    def countSquares(self, M: list[list[int]]) -> int:
        res = 0
        for q in range(len(M)):
            for u in range(len(M[0])):
                if M[q][u] == 1:
                    if q == 0 or u == 0:
                        res += 1
                    else:
                        cur = 1 + min(M[q - 1][u], M[q][u - 1], M[q - 1][u - 1])
                        res += cur
                        M[q][u] = cur
        return res

    def countVowelStrings(self, n: int) -> int:

        def F(n):
            if n == 1:
                return (5, 4, 3, 2, 1)
            else:
                t = F(n - 1)
                t0 = sum(t)
                t1 = t0 - t[0]
                t2 = t1 - t[1]
                t3 = t2 - t[2]
                t4 = t3 - t[3]
                return (t0, t1, t2, t3, t4)
         
        return F(n)[0]

 