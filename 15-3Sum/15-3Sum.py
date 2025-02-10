        """
        answer = set()
        N = len(nums)
        nums.sort()
        for i in range(N-2):
            j, k = i + 1, N - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
        for a,b,c in answer:
                    if (nums[i],nums[j],nums[k]) not in answer:
                        answer.add((nums[i],nums[j],nums[k]))
        x = []
            x.append([a,b,c])
        return x

