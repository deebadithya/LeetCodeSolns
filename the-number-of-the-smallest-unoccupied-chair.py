"""
the-number-of-the-smallest-unoccupied-chair.py

Code


Testcase
Test Result
Test Result
1942. The Number of the Smallest Unoccupied Chair
Solved
Medium
Topics
Companies
Hint
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.
For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.
You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.
Return the chair number that the friend numbered targetFriend will sit on.
"""

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key = lambda x: times[x][0])  # <-- 1)
        emptySeats, takenSeats = list(range(len(times))), []            # <-- 2)

        for i in order:                                                 # <-- 3)
            ar, lv = times[i]

            while takenSeats and takenSeats[0][0] <= ar:
                heappush(emptySeats, heappop(takenSeats)[1])
            seat = heappop(emptySeats)                                  # <-- 4)

            if i == targetFriend: return seat

            heappush(takenSeats,(lv, seat)) 

