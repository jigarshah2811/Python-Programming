from collections import defaultdict, deque
from typing import List


class Solution:

    def wordLadder(self, begin, end, words):
        L = len(words[0])  # Since every word is same len
        patternToWord = defaultdict(list)

        def construct_dict(words):
            for word in words:
                for i in range(L):
                    pattern = word[:i] + '-' + word[i+1:]
                    patternToWord[pattern].append(word)
            print("Phase 1: Constructing intermidiate pattern....")
            print(patternToWord)
        construct_dict(set(words))

        # BFS from beginWord to endWord
        q = deque()       # (Word, bfs-level, path)
        q.append((beginWord, 0, []))
        visited = set()
        visited.add(beginWord)
        while q:
            (word, bfsLevel, curPath) = q.popleft()

            print("Visiting Word: {}, bfsLevel: {}, curPath: {}".format(word, bfsLevel, curPath))
            conns = set()
            # Create connections list for curWord based on intermidiatery pattern
            for i in range(L):
                pattern = word[:i] + '-' + word[i+1:]
                someconns = patternToWord[pattern]  # Becomes connections
                conns = conns | set(someconns)

            print("Conns: {}".format(conns))
            # At this stage, all connections are formed word=hit, conns = ['git', 'hot']
            for conn in conns:
                if conn == endWord:  # Found the ending word
                    return curPath + [conn]
                if conn in visited:
                    continue
                q.append((conn, bfsLevel+1, curPath+[word]))
                visited.add(conn)


class SolutionOld:
    def ladderLength(self, beginWord, endWord, wordList):
        # Since all words are of same length.
        L = len(beginWord)

        # Phase 1: Create a {pattern: [word1, word2]} dict. i.e {'h*t':[hot, hit]}
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        patternToWord = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                patternToWord[pattern].append(word)

        # Phase 2: Start BFS from beginWord, create patterns from beginWord,
        queue = deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = set(beginWord)
        while queue:
            word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                pattern = word[:i] + "*" + word[i+1:]

                # Next states are all the words which share the same intermediate state.
                # print("word: {0}, patternToWord: {1}".format(pattern, patternToWord))
                # Find neighbor words that matches pattern and see if we reach targetWord
                connWords = patternToWord[pattern]
                for connWord in connWords:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if connWord == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if connWord not in visited:
                        visited.add(connWord)
                        queue.append((connWord, level + 1))
                patternToWord[pattern] = []
        return 0


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print((s.wordLadder(beginWord, endWord, wordList)))
