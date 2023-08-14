class Solution:
    def countBits(self, n: int) -> List[int]:
        return [sum(map(int, bin(i)[2:])) for i in range(n+1)]
        
