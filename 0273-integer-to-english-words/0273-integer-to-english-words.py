class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        
        tens_map = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        
        digits = [-1]*10
        i = 9
        while num > 0:
            digits[i] = num % 10
            i -= 1
            num //= 10
        answer = ""
        i = 0
        
        def resolve(digit):
            result = ""
            if digit[0] > 0:
                    result += ones_map[digit[0]] + " Hundred "
            if digit[1] > 0:
                if digit[1] == 1:
                    result += ones_map[digit[1]*10 + digit[2]] + " "
                elif digit[1] > 1:
                    result += tens_map[digit[1]] + " "
                    if digit[2] > 0:
                        result += ones_map[digit[2]] + " "
            elif digit[2] > 0:
                result += ones_map[digit[2]] + " "  
            return result
        while i < 10:
            if digits[i] == -1:
                i+=1
                continue
            if i == 0:
                answer += ones_map[digits[i]] + " Billion "
                i += 1
            elif i in [1,2,3]:
                temp = resolve(digits[1:4])
                if len(temp) > 0:
                    answer += temp + "Million "
                i = 4
            elif i in [4,5,6]:
                temp = resolve(digits[4:7])
                if len(temp) > 0:
                    answer += temp + "Thousand "
                i = 7
            else:
                answer += resolve(digits[7:10])
                i = 10
        return answer.strip()
            
        