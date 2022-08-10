#
# @lc app=leetcode.cn id=749 lang=python3
#
# [749] 隔离病毒
#

# @lc code=start
from typing import List


dir_c = (1, -1, 1j, -1j)


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        book = [set(), set()]
        for i, row in enumerate(isInfected):
            for j, c in enumerate(row):
                book[c].add(complex(i, j))
        blank, virus = book

        def dfs(u, infect, neib):
            if u in neib:
                return 0
            neib.add(u)
            wall = 0
            for v in (u+1, u-1, u+1j, u-1j):
                if v in blank:
                    infect.add(v)
                    wall += 1
                elif v in virus:
                    wall += dfs(v, infect, neib)
            return wall

        res = 0
        while virus and blank:
            seen = set()
            hi = (set(), set(), 0)
            book = []
            for u in virus:
                if u in seen:
                    continue
                infect, neib = set(), set()
                walls = dfs(u, infect, neib)
                seen.update(neib)
                book.append((infect, neib, walls))
                if len(hi[0]) < len(infect):
                    hi = (infect, neib, walls)

            res += hi[2]
            virus -= hi[1]
            for infect, neib, walls in book:
                if len(hi[0]) == len(infect):
                    continue
                if infect:
                    virus |= infect
                    blank -= infect
                else:
                    virus -= neib
        return res

# @lc code=end
