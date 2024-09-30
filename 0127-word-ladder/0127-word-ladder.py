class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neigh = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[0:j] + "*" + word[j+1:]
                neigh[pattern].append(word)
        
        visit = set([beginWord])        
        queue = collections.deque([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiPattern in neigh[pattern]:
                        if neiPattern not in visit:
                            queue.append(neiPattern)
                            visit.add(neiPattern)
            res += 1
        return 0
            
                
            
                
            
            
            
            