from QUEUE import Queue
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
"""
def visit(mylist):
    # Base case
    if not mylist:
        return

    for ele in mylist:
        if isinstance(ele, str):
            print ele
        else:
            # ele is again a list
            visit(ele)

visit(URL)
"""

"""
for URL1, ListURLs1 in URL.items():
    for URL2, ListURLs2 in ListURLs1.items():
        for URL3, ListURLs3 in ListURLs2.items():
            print URL3
"""


def WebCrawl_Helper(ListURLs, Depth, s):
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

    # BFS
    myqueue = Queue()
    myqueue.enqueue([ListURLs for URL, ListURLs in ListURLs.items()])

    while not myqueue.isEmpty():
        n = myqueue.size()
        while n != 0:
            VisitingURL = myqueue.dequeue()
            for URL, ListURLs in VisitingURL.items():
                s = WebCrawl_Helper(ListURLs, Depth-1, s)
            n -= 1
    return s


def WebCrawl(URL, Depth, s):

    for ele in URL:
        if isinstance(ele, str):
            s.add([ele])
        else:
            s = WebCrawl_Helper(ele, Depth-1, s)
    return s

s = set()
s = WebCrawl(URL, 2, s)

print len(s)
