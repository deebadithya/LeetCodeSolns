"""
check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence.py
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
Solved
Easy
Topics
Companies
Hint
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.
"""
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for ind, val in enumerate(sentence.split()):
            if val.startswith(searchWord):
                return ind + 1
        return -1
