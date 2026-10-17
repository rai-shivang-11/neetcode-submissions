class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vMap = {}
        for i in range(len(position)):
            vMap[position[i]] = speed[i]
        position.sort()
        position = position[::-1]
        fleet = 1
        prev = (target - position[0])/vMap[position[0]]
        for p in position[1:]:
            time = (target - p)/vMap[p]
            if time > prev:
                fleet += 1
                prev = time
        return fleet
