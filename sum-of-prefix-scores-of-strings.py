"""
sum-of-prefix-scores-of-strings.py
"""

from typing import List, Dict

# TIME LIMIT EXCEEDED
# class Solution:
#     def sumPrefixScores(self, words: List[str]) -> List[int]:
#         memo = {}
#         result_count = [0] * len(words)
#         for idx, word in enumerate(words):
#             sub_str_count = 0
#             for i in range(1, len(word)+1):
#                 temp_count = 0
#                 if word[:i] in memo: sub_str_count += memo[word[:i]]; continue
#                 for w in words:
#                     if i <= len(w) and word[:i] == w[:i]:
#                         temp_count += 1
#                 memo[word[:i]] = temp_count 
#                 sub_str_count += temp_count
#             result_count[idx] = sub_str_count       
#         return result_count
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Build the trie structure from the list of words
        trie = self.buildTrie(words)
        # Calculate and return the prefix scores for each word
        return self.calculatePrefixScores(trie, words)

    def buildTrie(self, words: List[str]) -> Dict:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                # Navigate through or create nodes in the trie
                node = node.setdefault(char, {})
                # Count occurrences of the prefix
                node['$'] = node.get('$', 0) + 1
        return trie

    def calculatePrefixScores(self, trie: Dict, words: List[str]) -> List[int]:
        scores = []
        for word in words:
            node = trie
            total_score = 0
            for char in word:
                # Move to the next node and accumulate the score
                node = node[char]
                total_score += node['$']
            scores.append(total_score)
        return scores
soln = Solution()
result = soln.sumPrefixScores(["abc","ab","bc","b"])
print(result)