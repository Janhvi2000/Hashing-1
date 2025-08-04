# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # Dictionary to hold keys

        for word in strs:
            count = [0] * 26  # Create a frequency count for each letter (a–z)

            for char in word:
                count[ord(char) - ord('a')] += 1  # Count occurrences of each letter

            # Convert the count list to unique key (e.g., "1#0#0#0#...#1")
            key = '#'.join(map(str, count))

            groups[key].append(word)  # Group words with the same character counts

        return list(groups.values())
