class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for _ in range(len(temperatures))]
        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                _, idx = stack.pop()
                answer[idx] = i - idx
            stack.append((n, i))

        return answer
        