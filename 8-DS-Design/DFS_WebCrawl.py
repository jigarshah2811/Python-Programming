URL = ['bbc.com',
       ['bbc.com/india',
            ['bbc.com/guj',
             'bbc.com/pun'
             ],
        'bbc.com/china',
            ['bbc.com/sanghai',
             'bbc.com/tokyo',
             'bbc.com/tokyo'
             ]
        ]
       ]


class Solution:
    def __init__(self, urls):
        self.urls = urls

    def dfs(self, depth):
        visited = set()
        visiting = set()  # To prevent cycle: Record the stack of URLs in process of visit
        for url in self.urls:
            if isinstance(url, str):
                self.visited.add(url)
            else:
                for suburl in urls:
                    self.visit(suburl, visited, visiting)

    def visit(self, url, visited, visiting):
        visiting.add(url)

        for conn in url:
            if conn in visiting:
                return
            elif conn not in visited:
                self.visit(conn)

        visited.add(url)
        visiting.remove(url)

def dfs(ListURLs, Depth, s):
    # Base Case, Max depth reached or empty children URL set
    if Depth == 0 or ListURLs == []:
        return

    listToVisit = list()
    # Remove duplicates and create global set
    for ele in ListURLs:
        if isinstance(ele, str):
            s.add([ele])
        else:
            # List
            listToVisit.append(ele)


def bfs(root_url, depth):
    # BFS
    q = [root_url]
    visited = set()

    while q:
        n = len(q)
        while n != 0:
            curURL = q.pop()
            for URL in curURL:
                if URL is not visited:
                    q.append(URL)
            n -= 1
        depth -= 1

def WebCrawl(URL, Depth, s):

    for ele in URL:
        if isinstance(ele, str):
            s.add(ele)
        else:
            s = dfs(ele, Depth-1, s)
    return s

s = set()
s = WebCrawl(URL, 2, s)

print(len(s))
