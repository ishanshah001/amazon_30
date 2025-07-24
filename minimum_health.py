class Solution:
    def minimumHealth(self, damage, armor):
        return sum(damage) - min(max(damage), armor) + 1


# We greedily use the armor at the level with the greatest damage. 
# Without armor, we need 1 + sum(A) min health. 
# The armor can take damange of min(max(A), armor), saving us this amount of health. 
# So in total, we just need 1 + sum(A) - min(max(A), armor)