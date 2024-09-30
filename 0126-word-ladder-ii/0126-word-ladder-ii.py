from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Adjacency list to store the graph
        adj = defaultdict(list)
        visited = set()
        queue = deque([beginWord])
        visited.add(beginWord)
        found = False

        while queue and not found:
            level_size = len(queue)
            current_level_visited = set()
            for _ in range(level_size):
                currentWord = queue.popleft()
                tempWord = currentWord

                for j in range(len(currentWord)):
                    originalChar = currentWord[j]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == originalChar:
                            continue  # Skip if character is the same as original
                        currentWord = currentWord[:j] + c + currentWord[j+1:]
                        if currentWord in wordSet:
                            if currentWord == endWord:
                                found = True
                            if currentWord not in visited:
                                if currentWord not in current_level_visited:
                                    queue.append(currentWord)
                                    current_level_visited.add(currentWord)
                                adj[currentWord].append(tempWord)
                    currentWord = tempWord  # Restore original character

            visited.update(current_level_visited)

        res = []
        if found:
            path = [endWord]
            self.backtrack(endWord, beginWord, adj, path, res)
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
