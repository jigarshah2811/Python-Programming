import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0]*numCourses

        def dfs(course):
            if visited[course] == -1:  # This was already in stack, so we came here again! LOOP
                print(f"LOOP: {course}")
                return False

            if visited[course] == 1:  # Course is already visited, no need to revisit
                return True
            
            # visiting
            visited[course] = -1
            print(f"Visiting: {course}")

            # Visit all conn
            for conn in graph[course]:
                if conn not in visited:  # Not already visisted
                    print(f"Visiting conn: {conn}")
                    if dfs(conn) == False:
                        return False

            # visited this course completely
            visited[course] = 1
            print(f"visisted {course}")

            return True



        graph = collections.defaultdict(list)
        for course in prerequisites:
            node, dep = course[0], course[1]
            graph[dep].append(node)
        
        # Check all courses (nodes)
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True

s = Solution()
# numCourses = 2; prerequisites = [[1,0]]
# print(s.canFinish(numCourses, prerequisites))       # output: True

# numCourses = 2; prerequisites = [[1,0],[0,1]]     
# print(s.canFinish(numCourses, prerequisites))       # output: False

numCourses = 5; prerequisites = [[1,0],[2, 1], [3, 2], [4, 1]]
print(s.canFinish(numCourses, prerequisites))       # output: True


numCourses = 5; prerequisites = [[1,0],[2, 1], [3, 2], [4, 1], [3, 1]]      # 1->2->3 fine
print(s.canFinish(numCourses, prerequisites))       # output: True


numCourses = 5; prerequisites = [[1,0],[2, 1], [3, 2], [4, 1], [1, 3]]      # 1->2->3->1 fine
print(s.canFinish(numCourses, prerequisites))       # output: False
