"""
uncommon-words-from-two-sentences.py
884. Uncommon Words from Two Sentences
Solved
Easy
Topics
Companies
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
"""
from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        dups = []
        for word in (s1 + " " + s2).split():
            if word not in dups:
                result.append(word)
                dups.append(word)
            elif word in result:
                result.remove(word)
        return result