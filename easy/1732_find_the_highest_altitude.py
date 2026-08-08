class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxx = 0
        for r in range(len(gain)):
            altitude += gain[r]
            
            if altitude > maxx:
                maxx = altitude
        return maxx
            

            