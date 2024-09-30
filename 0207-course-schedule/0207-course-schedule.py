class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses + 1):
            preMap[i] = list()
        for i in prerequisites:
            preMap[i[0]].append(i[1])
        
        path = []
        
        def dfs(course):
            if len(preMap[course]) == 0:
                return True
            if course in path:
                return False
            path.append(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            preMap[course] = []
            return True
        
        for i in range(numCourses):
            if len(preMap[i]) > 0:
                for pr in preMap[i]:
                    if not dfs(pr):
                        return False  
        return True



        