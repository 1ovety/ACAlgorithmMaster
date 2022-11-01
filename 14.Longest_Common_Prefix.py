class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0
        
        # uses string slices to take the first i letters of each string. 
        # At the beginning, these would all be empty strings. 
        # Casting to a set removes duplicates. For example, set([1, 2, 2, 3]) = {1, 2, 3}. 
        # By casting our list of prefixes to a set, we remove duplicates.
        while len(set([word[:i] for word in strs])) <= 1:
            
                i += 1
                
        return strs[0][:i-1]
        


