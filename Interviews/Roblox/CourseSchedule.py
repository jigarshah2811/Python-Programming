import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Build Graph and INDEGREE for topological sorting
        self.numCourses = numCourses
        self.graph = collections.defaultdict(list)
        self.indegree = [0]*numCourses

        for course, revdep in prerequisites:
            self.graph[revdep].append(course)
            self.indegree[course] += 1
            
        print(f"Graph -->   {self.graph}")
        for i, val in enumerate(self.indegree):
            print(f"indegree[{i}] = {val}")
        
        q = collections.deque()
        for course in range(self.numCourses):
            if self.indegree[course] == 0:  # This course has NO dependancies
                q.append(course)            # Queue up to finish
        
        res = []
        while q:    # Pop one-by-one course with NO dep and finish it
            course = q.popleft()    # This course is with indegree=0, so no dep
            res.append(course)
            for conn in self.graph[course]: # all courses that are UNBLOCKED due to this course is finish
                print(conn)
                self.indegree[conn] -= 1
                if self.indegree[conn] == 0:    # This course is READY to be finished
                    q.append(conn)

        # Check if ALL courses are finished
        if len(res) == self.numCourses:
            return res
        else:
            return []