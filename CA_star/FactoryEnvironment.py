import pygame
import numpy as np
from pygame.locals import RESIZABLE
from CA_star.path_planner import PathPlanner
from CA_star.grid import Grid


class FactoryEnvironment:
    # 定义grid map的大小（行和列）
    ROWS = 20
    COLS = 20

    # 定义每个格子的宽度和高度
    GRID_SIZE = 40

    # 定义颜色
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    # 计算屏幕尺寸
    SCREEN_WIDTH = COLS * GRID_SIZE
    SCREEN_HEIGHT = ROWS * GRID_SIZE

    def __init__(self, height, width, walls, agents):
        self.agents = agents
        self.height = height
        self.width = width
        self.walls = walls
        self.planned_path = {}

        # put it in Grid class
        self.grid_array = np.zeros(shape=(height, width), dtype=int)
        for (i, j) in self.walls:
            self.grid_array[i][j] = 1

        self.grid = Grid(self.height, self.width, self.walls)
        self.path_planner = PathPlanner(self.grid)

        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), RESIZABLE)

    def draw_grid_map(self, grid_map):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid_map[row][col] == 1:
                    color = self.BLACK
                elif grid_map[row][col] == 0:
                    color = self.WHITE
                else:
                    color = (grid_map[row][col] * 5 % 255, grid_map[row][col] * 7 % 255, grid_map[row][col] * 2 % 255)
                pygame.draw.rect(self.screen, color, (col * self.GRID_SIZE, row * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))

    def plan_path_for_all_agents(self):
        for agent in self.agents:
            planned_path = self.path_planner.ca_star(agent.start, agent.destination)
            self.planned_path[agent.id] = planned_path
            time = 0
            for location in planned_path:
                self.grid.space_time_resource_utilization[(location[0], location[1], time)] = agent.id
                time += 1

    def main(self):
        self.plan_path_for_all_agents()
        time = 0
        clock = pygame.time.Clock()
        # 游戏主循环
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            current_grid_map = np.array(self.grid_array)
            # for () in planned_path
            for agent_id in self.planned_path.keys():
                path = self.planned_path.get(agent_id)
                if time < len(path):
                    (x, y) = path[time]
                    current_grid_map[x][y] = agent_id

            time += 1

            # 填充背景颜色

            self.screen.fill(self.WHITE)

            # 画grid map
            self.draw_grid_map(current_grid_map)

            clock.tick(2)

            # 更新屏幕
            pygame.display.flip()

        # 退出Pygame
        pygame.quit()

