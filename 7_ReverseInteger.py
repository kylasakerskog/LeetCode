class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x > 2**31-1 or x < -2**31):
            return 0
        else:
            x_str = str(x)
            if(x >= 0):
                reversed = x_str[::-1]                
            else:
                tmp = x_str[1:]
                reversed = "-" + tmp[::-1]
                print(reversed)
            if int(reversed) > 2**31-1 or int(reversed) < -2**31:
                return 0
            else: return int(reversed)

"""
s=Solution()
print(s.reverse(-123))
"""
