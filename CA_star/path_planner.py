from CA_star.grid import Grid
import queue


class PathPlanner:
    def __init__(self, grid: Grid):
        self.grid = grid

    def heuristic_cost(self, current_location, destination):
        (x1, y1) = current_location
        (x2, y2) = destination

        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, start, destination, came_from):
        current_location = destination
        path = []

        if destination not in came_from:
            return []

        while (current_location[0], current_location[1]) != start:
            (x, y, t) = current_location
            path.append((x, y))
            current_location = came_from[current_location]
        path.append(start)
        path.reverse()

        return path

    def ca_star(self, start, destination):
        frontier = queue.PriorityQueue()
        start_space_time_location = (start[0], start[1], 0)
        frontier.put([0, start_space_time_location])
        came_from = {}
        cost = {}
        came_from[start_space_time_location] = None
        cost[start_space_time_location] = 0
        current_space_time_location = tuple()

        time = 0
        current_location = None
        while current_location != destination:
            current_space_time_location = frontier.get()[1]
            current_location = (current_space_time_location[0], current_space_time_location[1])

            for next_space_time_location in self.grid.neighbors(current_space_time_location):
                # 可改成停下來cost+=1, 走一步cost+=2
                new_cost = cost[current_space_time_location] + 1

                if next_space_time_location not in cost.keys() or new_cost < cost[next_space_time_location]:
                    cost[next_space_time_location] = new_cost
                    priority = new_cost + self.heuristic_cost((next_space_time_location[0], next_space_time_location[1]), destination)
                    #priority = self.heuristic_cost((next_space_time_location[0], next_space_time_location[1]), destination)
                    frontier.put([priority, next_space_time_location])
                    came_from[next_space_time_location] = current_space_time_location

            time += 1
        planned_path = self.reconstruct_path(start, current_space_time_location, came_from)

        return planned_path
