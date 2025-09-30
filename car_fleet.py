class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time = []
        pos_and_spd = [[] for i in range(len(position))]
        for i in range(len(position)):
            pos_and_spd[i] = [position[i], speed[i]]
        pos_and_spd = sorted(pos_and_spd)
        for i in range(len(pos_and_spd)):
            time.append((target - pos_and_spd[i][0]) / pos_and_spd[i][1])
        for i in range(len(time)-1, -1, -1):
            if time[i] >= time[i-1] and i >= 1:
                time.pop(i-1)
        return len(time)