class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(n):
            sum = 0
            while n:
                sum += (n%10)**2
                n = n//10
            return sum
        a = set()
        while True:
            if n == 1:
                return True
            if n in a:
                return False
            a.add(n)
            n = squareSum(n)
            
