from FactoryEnvironment import FactoryEnvironment
from agent import Agent


obstacles = [(x, y) for x in range(0, 8) for y in range(5, 15)] + [(x, y) for x in range(12, 20) for y in range(5, 15)]
agents = []
for i in range(0, 6):
    agents.append(Agent())
agents[0].set_task((0, 0), (19, 19), 0)
agents[1].set_task((19, 19), (0, 0), 1)
agents[2].set_task((19, 0), (0, 19), 2)
agents[3].set_task((0, 19), (19, 0), 3)
agents[4].set_task((18, 0), (1, 0), 4)
agents[5].set_task((0, 18), (0, 0), 10)
environment = FactoryEnvironment(20, 20, obstacles, agents)
environment.main()

# to-do:
# FactoryEnvironment 類別中加入set_number_of_agents, set_task等功能，以更好的封裝
# PathPlanner 僅規劃路線，無任務時agent不會佔用時空間資源。可在Grid中新增一矩陣記錄所有靜止agent的位置，或是直接給予agent停留原地的task
# 之類的方法，總之要讓agent在沒有任務時也占用一格時空間資源
