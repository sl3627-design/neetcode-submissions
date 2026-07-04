class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        end_time = [sum(customers[0])]

        for i in range (1, len(customers)):
            end_time.append(max(sum(customers[i]), end_time[-1] + customers[i][1]))
        
        tot = 0

        for i in range (len(end_time)):
            tot += end_time[i] - customers[i][0]
        
        return tot/len(end_time)