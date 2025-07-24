class Solution:
    def largestVariance(self, s: str) -> int:
        def solveOne(a, b, string):
            max_var = 0
            
            var = 0
            has_b = False
            first_b = False # first element of the currently considered subarray is b
            
            for c in string:
                if c == a:
                    var += 1
                
                elif c == b:
                    has_b = True
                    # check if first b (b exists) is already reached and again another b doesnot come
                    if first_b and var >= 0: 
                        first_b = False 
                    # it means either b is not reached or back to back like baa or bba..
                    elif (var - 1) < 0:
                        first_b = True 
                        var = -1
                    else:
                        var -= 1
                
                if has_b and var > max_var:
                    max_var = var
            
            return max_var
        
        max_variance = 0
        unique = list(set(s))
        for a in unique: #     see below
            for b in unique: # rules dictate these 2 loops would be no more than O(26*26)
                if a == b: continue
                a_against_b_var = solveOne(a, b, s) # <= you want to do this efficiently
                max_variance = max(a_against_b_var, max_variance)

        return max_variance 