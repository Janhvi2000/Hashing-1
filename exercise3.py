class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # Split the input string into words
        strings = s.split(' ')

        # Pattern and word list must be of the same length
        if len(pattern) != len(strings):
            return False

        # Create mappings: pattern character → word, and word → pattern character
        mapptos = {}
        mapstop = {}

        # Iterate through both pattern and words simultaneously
        for char, word in zip(pattern, strings):
            # If there's already a mapping, ensure it's consistent
            if (char in mapptos and mapptos[char] != word) or (word in mapstop and mapstop[word] != char):
                return False  # Inconsistent mapping found

            # Save the mapping in both directions
            mapptos[char] = word
            mapstop[word] = char

        # If all mappings are consistent, return True
        return True
