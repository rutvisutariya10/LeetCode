class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ransom = {}
        maga = {}
        for i in ransomNote:
            ransom[i] = ransom.get(i,0) + 1
        for i in magazine:
            maga[i] = maga.get(i,0) + 1
        print(ransom,maga)
        for i in ransom.keys():
            if i not in maga:
                return False
            if ransom[i] > maga[i]:
                return False
        return True
        