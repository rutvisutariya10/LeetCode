class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the closest
        closest = 0
        arr.sort()
        diff = float("inf")
        for i,num in enumerate(arr):
            curr = abs(num-x)
            if curr < diff or (curr == diff and num < arr[closest]):
                diff = curr
                closest = i
        answer = [arr[closest]]
        l,r = closest-1,closest+1
        while l >= 0 and r < len(arr):
            diff_x = abs(arr[l] - x)
            diff_y = abs(arr[r] - x)
            
            if diff_x > diff_y:
                answer.append(arr[r])
                r += 1
            else:
                answer.append(arr[l])
                l -= 1
        while l >= 0:
            answer.append(arr[l])
            l -= 1
        while r < len(arr):
            answer.append(arr[r])
            r += 1
        return sorted(answer[:k])
        
        
            
        