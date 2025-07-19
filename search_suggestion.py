class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        left = 0
        right = len(products)
        op=[]
        for i in range(len(searchWord)):
            result = []
            for j in range(left, right):
                if searchWord[:i+1]==products[j][:i+1]:
                    result.append(products[j])
                    if len(result)==3:
                        break
            op.append(result)
        return op
                    
