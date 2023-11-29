class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num).replace('0b','')
        t = ''
        for a in s:
            if a == '1':
                t += '0'
            else:
                t += '1'
        return int(t,2)
