                    number -= (2 ** power)
                    answer[n] = '1'
                power -= 1
            return ''.join(answer)
        for n in nums:
            numbers.add(to_decimal(n))
        for i in range(2**L):
            if i not in numbers:
                return to_binary(i)
        

