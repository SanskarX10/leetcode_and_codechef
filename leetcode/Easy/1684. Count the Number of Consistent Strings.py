"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            for char in w:
                if char not in allowed:
                    count += 1
                    break
        return len(words) - count

        
