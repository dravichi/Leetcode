class Solution:
    def isValid(self, s: str) -> bool:
        o = []
        for i in s:
            if i == '(':
                o.append(')')
            elif i == '[':
                o.append(']')
            elif i == '{':
                o.append('}')
            else:
                if len(o) != 0 and i == o[-1]:
                    o.pop()
                else:
                    return False
        return len(o) == 0
        
