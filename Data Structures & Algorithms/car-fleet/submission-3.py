class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vMap = {}
        for i in range(len(position)):
            vMap[position[i]] = speed[i]
        position.sort()
        position = position[::-1]
        fleet, temp = 1, 0
        prev = (target - position[0])/vMap[position[0]]
        #prev = 10000000000
        for p in position[1:]:
            time = (target - p)/vMap[p]
            if time <= prev:
                temp += 1
            else:
                fleet += 1
                temp = 0
                prev = time
        return fleet
