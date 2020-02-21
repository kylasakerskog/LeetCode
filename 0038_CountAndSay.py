class Solution(object):
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(1,n):
            s = self.cal(s)  
        return s
        
    def cal(self, s):
        count = 0
        current_s = s[0]
        return_string = ""
        for i in range(len(s)):
            if s[i] == current_s:
                count += 1
            else:
                return_string += str(count)
                return_string += current_s
                count = 1
                current_s = s[i]
        return_string += str(count)
        return_string += current_s
        return return_string
