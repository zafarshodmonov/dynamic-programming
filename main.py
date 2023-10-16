
class DynamicProgramming:
    
    def f(self, n: int):
        if n == 1:
            return 1
        return self.f(n - 1) + 1
    
    def fib_map(self, n: int, memo = {}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = self.fib_map(n - 2, memo) + self.fib_map(n - 1, memo)
        return memo[n]
    
    def fib_list(self, n: int, memo = None):
        if memo is None:
            memo = [1 if i == 1 and i == 2 else None for i in range(n + 1)]
        if memo[n] is not None:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = self.fib_list(n - 2, memo) + self.fib_list(n - 1, memo)
        return memo[n]
    
    def dib(self, n: int):
        count += 2
        if n <= 1:
            return
        self.dib(n - 1)
        self.dib(n - 1)
    
    def lib(self, n: int):
        if n <= 1:
            return
        self.lib(n - 2)
        self.lib(n - 2)
    

def main() -> None:
    dp = DynamicProgramming()
    print("Natija: ", dp.fib_list(5))

if __name__ == "__main__":
    main()
