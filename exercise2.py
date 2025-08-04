# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charmap_s = defaultdict(list)
        charmap_t = defaultdict(list)
        
        # Iterate through characters of both strings simultaneously
        for char_s, char_t in zip(s, t):
            # If char_s has been seen before in charmap_s, it must always map to the same char_t, or it's not isomorphic
            if charmap_s[char_s]:
                if charmap_s[char_s] != [char_t]: 
                    return False
            else:
                # First time seeing char_s, store the mapping to char_t
                charmap_s[char_s].append(char_t)
            
            if charmap_t[char_t]: 
                if charmap_t[char_t] != [char_s]: 
                    return False
            else:
                charmap_t[char_t].append(char_s)
        
        # All characters matched one-to-one in both directions
        return True
