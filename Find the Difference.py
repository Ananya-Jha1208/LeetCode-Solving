class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for cs in s: c ^= ord(cs) #ord is ASCII value
        for ct in t: c ^= ord(ct)
        return chr(c) #chr = convert ASCII into character


# Let:
# s = abc
# t = cabx

# if we take XOR of every character. all the n characters of s "abc" that are similar to n characters of t "cab" will cancel each other out and we are left with our answer.

# s =   abc
# t =   cbax
# ------------
# ans -> x
# -----------
