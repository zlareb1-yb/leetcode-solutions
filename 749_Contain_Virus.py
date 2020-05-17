# https://leetcode.com/problems/contain-virus/

"""
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as a 2-D array of cells, where 0 represents uninfected cells, and 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region -- the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night. There will never be a tie.

Can you save the day? If so, what is the number of walls required? If not, and the world becomes fully infected, return the number of walls used.
"""


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def adj_cells(row, col):
            for r, c in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if 0 <= r < rows and 0 <= c < cols:
                    yield r, c

        def no_of_elements_in_2d_list(list_2d):
            return sum(len(li) for li in list_2d)

        def get_contaminated_areas():
            areas = []
            dangers = []
            walls = []
            seen = [[False] * cols for i in range(rows)]

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and not seen[r][c]:
                        area = [(r, c)]
                        danger = set()
                        queue = [(r, c)]
                        seen[r][c] = True
                        wall = 0

                        while queue:
                            m, n = queue.pop(0)
                            for i, j in adj_cells(m, n):
                                index = (i, j)
                                if grid[i][j] == 1 and not seen[i][j]:
                                    seen[i][j] = True
                                    queue.append(index)
                                    area.append(index)
                                elif grid[i][j] == 0:
                                    wall += 1
                                    danger.add(index)
                        areas.append(area)
                        dangers.append(danger)
                        walls.append(wall)

            return areas, dangers, walls

        def spread_virus(dangers):
            for danger in dangers:
                for row, col in danger:
                    grid[row][col] = 1

        wall = 0
        areas, dangers, walls = get_contaminated_areas()

        while areas:
            area_count = len(areas)

            if no_of_elements_in_2d_list(areas) == rows * cols:
                return wall

            dangerest_index = 0

            for i in range(area_count):
                if len(dangers[i]) > len(dangers[dangerest_index]):
                    dangerest_index = i

            wall += walls[dangerest_index]

            for i, j in areas[dangerest_index]:
                grid[i][j] = -1

            spread_virus(dangers[:dangerest_index] + dangers[dangerest_index + 1 :])

            areas, dangers, walls = get_contaminated_areas()

        return wall
