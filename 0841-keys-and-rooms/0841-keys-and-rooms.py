from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        q = deque()
        visited[0] = True
        q.append((0, rooms[0]))
        while q:
            _, keys = q.popleft()
            for next_room in keys:
                if not visited[next_room]:
                    visited[next_room] = True
                    q.append((next_room, keys+rooms[next_room]))
        
        if all(visited) :
            return True
        else:
            return False

                