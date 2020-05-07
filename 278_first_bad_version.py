# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.searchBadVersion(1, n)

    def searchBadVersion(self, start, end):
        if start <= end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                return self.searchBadVersion(mid + 1, end)
            elif isBadVersion(mid - 1):
                return self.searchBadVersion(start, mid - 1)
            else:
                return mid
