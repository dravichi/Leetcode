class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if digits:
            def gen(temp, no):
                if no == len(digits):
                    res.append(temp)
                    return
                no += 1
                for i in d[digits[no-1]]:
                    gen(temp+i, no)
            gen('', 0)
        return res
