# 17. Letter Combinations of a Phone Number
"""
Runtime: 20 ms, faster than 97.10% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        l_digits = []
        results = []
        nw = {'2': ['a', 'b', 'c']
               ,'3': ['d', 'e', 'f']
               ,'4': ['g', 'h', 'i']
               ,'5': ['j', 'k', 'l']
               ,'6': ['m', 'n', 'o']
               ,'7': ['p', 'q', 'r', 's']
               ,'8': ['t', 'u', 'v']
               ,'9': ['w', 'x', 'y', 'z']
               }
        
        for i in digits:
            l_digits.append(nw[i])
        # アンバック
        for v in itertools.product(*l_digits):
            results.append("".join(v))
            
        return results
