from collections import defaultdict, Counter
from typing import List
from operator import itemgetter

class Solution:
    def mostVisitedPattern(self, usernames: List[str], timestamps: List[int], websites: List[str]) -> List[str]:
        # Step 1: Group websites visited by each user in chronological order
        visits = defaultdict(list)
        for user, _, site in sorted(zip(usernames, timestamps, websites), key=itemgetter(1)):
            visits[user].append(site)

        # Step 2: Count unique 3-sequences for each user
        pattern_count = Counter()
        for sites in visits.values():
            if len(sites) < 3:
                continue
            unique_patterns = set(
                (sites[i], sites[j], sites[k])
                for i in range(len(sites) - 2)
                for j in range(i + 1, len(sites) - 1)
                for k in range(j + 1, len(sites))
            )
            pattern_count.update(unique_patterns)

        # Step 3: Helper to sort by frequency (desc) then lex order
        def sort_key(item):
            return (-item[1], item[0])
        
        return min(pattern_count.items(), key=sort_key)[0]
