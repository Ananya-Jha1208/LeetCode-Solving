class Solution:
    def fib(self, n: int) -> int:
        fibn = [0,1]
        for i in range (2, n+1):
            fibn.append(fibn[i-1]+fibn[i-2])
        return fibn[n]
