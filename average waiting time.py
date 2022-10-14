class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        prev=0
        for i,j in customers:
            if prev<i:
                prev=i+j
                total+=j
            else:
                total+=(prev-i)+j
                prev +=j
        return total/len(customers)