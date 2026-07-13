class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the sliding window and character frequency map
        l = 0
        max_freq = 0  # Max frequency of a character in the current window
        char_count = {}

        # Iterate over the string with the right pointer `r`
        for r in range(len(s)):
            # Count the current character in the window
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            
            # Update max frequency in the current window
            max_freq = max(max_freq, char_count[s[r]])

            # If the number of characters that need to be replaced is greater than k,
            # shrink the window by moving the left pointer `l` to the right
            if (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1

        # The length of the longest substring with at most `k` replacements
        return r - l + 1