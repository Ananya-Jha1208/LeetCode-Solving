class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        l = len(timeSeries)
        for i in range(l):
        
            if i < l - 1:

                if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                    total += duration
                
                else:
                    total += timeSeries[i+1] - timeSeries[i]
        
            else:
                total += duration
        
        return total
