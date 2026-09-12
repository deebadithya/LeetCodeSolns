"""
remove-sub-folders-from-the-filesystem.py
1233. Remove Sub-Folders from the Filesystem
Solved
Medium
Topics
Companies
Hint
Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/
"""
from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        return result

