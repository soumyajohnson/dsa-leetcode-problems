class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        keys=[0]
        visited.add(0)
        while keys:
            room=keys.pop()
            visited.add(room)
            for r in rooms[room]:
                if r not in visited:
                    keys.append(r)
        return len(visited)==len(rooms)