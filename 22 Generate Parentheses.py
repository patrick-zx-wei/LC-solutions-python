class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #approach in a tree structure, options to open or close bracket
        def form(curr: str, l: int, r: int) -> List[str]:
            if r == 0:
                return [curr]
            ls = []
            if l > 0:
                nextl = curr + ("(") 
                ls.extend(form(nextl, l - 1, r))
            if l < r:
                nextr = curr[:] + (")")
                ls.extend(form(nextr, l, r - 1))
            return ls
        return form("(", n - 1, n)
            
