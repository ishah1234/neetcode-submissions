class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        target = {}
        for c in t:
            target[c] = target.get(c,0) + 1
        curr = {}
        match, l = 0, 0
        total = len(target)
        res = ""
        resLen = float("inf")
        for r in range(len(s)):
            c = s[r]
            curr[c] = curr.get(c, 0) + 1
            if c in target and curr[c] == target[c]:
                match += 1 
            while match == total:
                if (r -l + 1) < resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                curr[s[l]] -= 1
                if s[l] in target and curr[s[l]] < target[s[l]]:
                    match -= 1
                l += 1
        return res        