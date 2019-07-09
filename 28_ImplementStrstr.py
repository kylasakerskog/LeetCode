class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_ind = 0
        h_len = len(haystack)
        n_len = len(needle)
        if h_len == 0 and n_len == 0:
            return 0
        for h_ind in range(h_len):
            if haystack[h_ind:h_ind+n_len] == needle:
                return h_ind
        
        return -1
