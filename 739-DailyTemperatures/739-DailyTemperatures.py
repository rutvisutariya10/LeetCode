class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        73 69 70 74
        stack = [(73,0),(69,1),]
        '''
        stack = []
        answer = [0] * len(temperatures)
        for i,tem in enumerate(temperatures):
            while stack and stack[-1][0] < tem:
                currtem, curri = stack.pop()
                answer[curri] = i - curri
            stack.append((tem,i)) 
        return answer

