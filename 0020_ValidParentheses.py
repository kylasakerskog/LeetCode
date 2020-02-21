class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        if(len(s) != 0):
            l.append(s[0])
        for i in range(1,len(s)):
            if(len(l) == 0):
                l.append(s[i])
            elif((s[i]==')' and l[len(l)-1]=='(') or ((s[i]=='}' or s[i]==']') and l[len(l)-1]==chr(ord(s[i])-2))):
                l.pop()
            else:
                l.append(s[i])
        return len(l)==0
            
