class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_stack = []
        out = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            # if len(t_stack) == 0: 
            #     t_stack.append([i,t])
            #     continue

            while t_stack and (t > t_stack[-1][1]):
                j = t_stack[-1][0]
                k = i - j
                out[j] = k
                t_stack.pop()
            
            t_stack.append([i,t])

        return out