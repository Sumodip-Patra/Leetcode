class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])

        class Trie:
            def __init__(self):
                self.children = {}
                self.word = None

        root = Trie()

        for word in words:
            node = root

            for i in word:
                if i not in node.children:
                    node.children[i] = Trie()

                node = node.children[i]

            node.word = word

        res = []

        def dfs(r, c, node):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            ch = board[r][c]

            if ch == '#' or ch not in node.children:
                return

            node = node.children[ch]

            if node.word is not None:
                res.append(node.word)
                node.word = None

            board[r][c] = '#'

            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)

            board[r][c] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res