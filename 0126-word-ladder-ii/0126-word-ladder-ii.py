class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        remaining = set(wordList)
        remaining.discard(beginWord)
        distance = {beginWord: 1}
        queue = deque([beginWord])
        length = len(beginWord)

        def neighbors(word):
            for i in range(length):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + ch + word[i + 1:]
                    if candidate != word:
                        yield candidate

        while queue:
            word = queue.popleft()
            if word == endWord:
                break
            for candidate in neighbors(word):
                if candidate in remaining:
                    remaining.remove(candidate)
                    distance[candidate] = distance[word] + 1
                    queue.append(candidate)

        answer = []
        if endWord not in distance:
            return answer
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                answer.append(path[::-1])
                return
            for candidate in neighbors(word):
                if distance.get(candidate) == distance[word] - 1:
                    path.append(candidate)
                    dfs(candidate)
                    path.pop()

        dfs(endWord)
        return answer