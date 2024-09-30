class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for i in prerequisites:
            preMap[i[0]].append(i[1])
        
        order = []
        path,visit = set(),set()
        
        def dfs(course):
            if len(preMap[course]) == 0:
                if course not in visit:
                    visit.add(course)
                    order.append(course)
                return True
            if course in path:
                return False
            path.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            if course not in visit: 
                order.append(course)
                visit.add(course)
            path.remove(course)
            preMap[course] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
                