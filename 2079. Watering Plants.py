class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can = capacity
        step = 0
        for i in range(len(plants)):
            if plants[i] >= can:
                step += 2*i
                can = capacity
            
            can -= plants[i]
            step += 1

        return step