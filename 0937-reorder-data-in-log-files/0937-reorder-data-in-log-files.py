class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []    
        for log in logs:
            splitLog = log.split(" ")
            idt = splitLog[0]
            remaining = splitLog[1:]
            if remaining[0][0].isalpha():
                letters.append((remaining,idt))
            else:
                digits.append(log)
        letters.sort()
        answer = []
        for letterLog,idt in letters:
            answer.append(idt + " " + " ".join(letterLog))
        return answer + digits
        