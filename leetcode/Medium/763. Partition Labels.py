"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

"""




class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dict = {i : s.rfind(i) for i in s}

        size, res = 0, []
        end = dict[s[0]]
        
        for i in range(len(s)):
            
            size += 1
            end = max(end, dict[s[i]])

            if i == end:
                res.append(size)
                size = 0
                
        return res
