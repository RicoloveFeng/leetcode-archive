    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m={}
        slen = len(s)
        maxlen = 0
        first = 0
        last = 0
        while last != slen:
            if s[last] in m:
                maxlen = max(maxlen, last - first)
                first = max(m[s[last]] + 1, first)
            m[s[last]] = last
            last += 1
        return max(maxlen, slen - first)
