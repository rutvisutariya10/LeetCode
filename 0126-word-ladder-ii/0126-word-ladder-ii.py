from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Adjacency list to store the graph
        adj = {}
        neigh = collections.defaultdict(list)
        for word in wordSet:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                neigh[pattern].append(word)
        for word in wordSet:
            adj[word] = []
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neighbour in neigh[pattern]:
                    if neighbour != word:
                        adj[word].append(neighbour)
            
        visited = set()
        queue = deque([beginWord])
        backtrack_dict = collections.defaultdict(list)
        visited.add(beginWord)
        found = False

        while queue and not found:
            level_size = len(queue)
            current_level_visited = set()
            for _ in range(level_size):
                currentWord = queue.popleft()
                
                for word in adj[currentWord]:
                    if word == endWord:
                        found = True
                    if word not in visited:
                        if word not in current_level_visited:
                            queue.append(word)
                            current_level_visited.add(word)
                        if word != currentWord:
                            backtrack_dict[word].append(currentWord)
                            
            visited.update(current_level_visited)

        res = []
        if found:
            path = [endWord]
            self.backtrack(endWord, beginWord, backtrack_dict, path, res)
        return res

    def backtrack(self, currentWord: str, beginWord: str, adj: dict, path: List[str], res: List[List[str]]):
        if currentWord == beginWord:
            result = path.copy()
            result.reverse()
            res.append(result)
            return
        for nextWord in adj[currentWord]:
            path.append(nextWord)
            self.backtrack(nextWord, beginWord, adj, path, res)
            path.pop()