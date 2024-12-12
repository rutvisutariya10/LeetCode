# try to find easy solution first always
# here LCS was not required
# no need to complicate it everytime
# first think of simple solution always
# if that doesnt seem possible, go for advanced ds

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        found = []
        max_len = 0
        for word in dictionary:
            wordLen = len(word)
            c, w = 0, 0
            while c < len(s) and w < wordLen:
                if s[c] == word[w]:
                    w += 1
                    if w == wordLen:
                        if wordLen > max_len:
                            max_len = wordLen
                            found = [word]
                        elif wordLen == max_len:
                            found.append(word)
                        break
                c += 1
        found.sort()
        
        return found[0] if found else ""
                    
        