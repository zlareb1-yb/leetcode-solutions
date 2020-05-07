# https://leetcode.com/problems/jewels-and-stones


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        jewels = 0
        for ch in S:
            if ch in J:
                jewels += 1
        return jewels
