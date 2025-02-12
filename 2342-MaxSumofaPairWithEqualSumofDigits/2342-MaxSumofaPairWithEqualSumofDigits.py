            summ = 0
            while num > 0:
                summ += num % 10
                num //= 10
            if len(dict[summ]) < 2:
                dict[summ].append(nums[i])
            else:
                dict[summ].append(nums[i])
        filtered_dict = {k: v for k, v in dict.items() if len(v) == 2}
                dict[summ].sort(reverse = True)
                dict[summ].pop()
        sum_dict = {k: sum(v) for k, v in filtered_dict.items()}
        return max(sum_dict.values()) if sum_dict else -1



        
