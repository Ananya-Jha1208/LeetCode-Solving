class Solution:
    def canPlaceFlowers(self, f: List[int], n: int, i=0) -> bool:
        n -= not (f[i] or f[max(0, i-1)] or f[min(len(f)-1, i+1)])
        f[i] = f[i] if f[i] or f[max(0, i-1)] or f[min(len(f)-1, i+1)] else 1
        return n <= 0 if i == len(f)-1 else self.canPlaceFlowers(f, n, i+1)
