class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def div(n):
            for a in str(n):
                if a == '0' or n % int(a) > 0:
                    return False
            return True
        ans = []
        for n in range (left, right+1):
            if div(n):
                ans.append(n)
        return ans
