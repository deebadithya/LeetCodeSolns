"""
grumpy-bookstore-owner
"""

class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        # initilizing satisfied_customers that stores the max amount of customers saved by grumpy ctrl.
        already_satisfied = 0
        satisfied_customers = 0
        for i in range(0, len(customers)):
            scale_of_benefit = 0
            if i < (len(customers) - minutes + 1):
                for j in range(i,i+minutes):
                    if grumpy[j]:
                        scale_of_benefit += customers[j]
                if scale_of_benefit > satisfied_customers:
                    satisfied_customers = scale_of_benefit
            if not grumpy[i]:
                already_satisfied += customers[i]

        return already_satisfied + satisfied_customers