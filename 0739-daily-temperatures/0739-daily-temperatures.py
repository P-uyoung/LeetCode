class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for _ in range(len(temperatures))]
        for i, n in enumerate(temperatures):
            if not stack or n <= stack[-1][0]:
                stack.append((n, i))
            else:
                while stack:
                    if stack[-1][0] >= n: break
                    _, idx = stack.pop()
                    answer[idx] = i - idx
                stack.append((n, i))

        return answer
        