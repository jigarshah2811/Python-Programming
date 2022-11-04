""" DS: Freq Map     Pattern: Prefix Map (instead of using TRIE) 
    Pattern: String Manipulation
"""
class Solution:
    def subdomainVisits(self, inputList):
        seen = collections.defaultdict(int)
        
        # Go through each domain ---->
        for entry in inputList:
            count, domain = entry.split(" ")
            count = int(count)
            seen[domain] += count
            
            # Figure parent domains, mark all of them seen
            while True:
                dotIndex = domain.find(".")
                if dotIndex == -1:  # No more subdomain exists, Example: from leetcode.com --> com
                    break
                domain = domain[dotIndex+1:]
                seen[domain] += count
                
        print(seen)
        
        res, resStr = [], ""
        for domain, count in seen.items():
            resStr = f"{count} {domain}"
            res.append(resStr)
        
        return res
                
                