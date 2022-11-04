""" DS: Freq Map     Pattern: Prefix Map (instead of using TRIE) """
class Solution:
    def subdomainVisits(self, inputList: List[str]) -> List[str]:
        d = collections.defaultdict(int)
        
        for inputStr in inputList:
            inputItems = inputStr.split(" ")
            count, domain = inputItems[0], inputItems[1]
            
            d[domain] += int(count)
            
            # Also mark every parent domain as visited
            for i, c in enumerate(domain):
                if c == ".":
                    # everything from here on is parent domain
                    d[domain[i+1:]] += int(count)
                                        
        res = []
        for visitedDomain, count in d.items():
            res.append(str(count) + " " + visitedDomain)
        
        return res