class Solution:
    def romanToInt(self, s: str) -> int:
        
        rti = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0

        for a in range(len(s)-1):
            if (rti[s[a]] < rti[s[a+1]]):
                result = result - rti[s[a]]
            else:
                result = result + rti[s[a]]

        return (result + rti[s[-1]])
        
