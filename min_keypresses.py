from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        character_frequency = Counter(s)
      
        total_key_presses = 0
      
        allocated_keys, current_multiplier = 0, 1
      
        for frequency in sorted(character_frequency.values(), reverse=True):
            allocated_keys += 1
            total_key_presses += current_multiplier * frequency
        
            if allocated_keys % 9 == 0:
                current_multiplier += 1
      
        return total_key_presses