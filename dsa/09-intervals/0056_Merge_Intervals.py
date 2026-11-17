# It was hard to visualise at first
# but we only need to compare 1st end and 2nd start for overlap

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for s,e in intervals[1:]: #s,e new interval
            if s <= merged[-1][1]:
                merged[-1][1] = max([merged[-1][1], e]) 
            else:
                merged.append([s,e])
        return merged 
