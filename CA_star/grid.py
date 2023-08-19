# manage time and space
class Grid:
    def __init__(self, height, width, walls: list):
        self.height = height
        self.width = width
        self.walls = walls
        self.space_time_resource_utilization = {}

    def is_in_bounds(self, space_time_location):
        (x, y, t) = space_time_location
        return (0 <= x < self.width) and (0 <= y < self.height)

    def is_passable(self, space_time_location):
        (x, y, t) = space_time_location
        return (x, y) not in self.walls

    def is_collision_free(self, space_time_location, next_space_time_location, time):
        if next_space_time_location in self.space_time_resource_utilization.keys():
            return False

        next_location_at_current_moment = (next_space_time_location[0], next_space_time_location[1], time)
        current_location_at_next_moment = (space_time_location[0], space_time_location[1], time + 1)
        if next_location_at_current_moment in self.space_time_resource_utilization.keys() and current_location_at_next_moment in self.space_time_resource_utilization.keys():
            if self.space_time_resource_utilization[next_location_at_current_moment] == \
                    self.space_time_resource_utilization[current_location_at_next_moment]:
                return False

        return True

    def neighbors(self, space_time_location):
        (x, y, time) = space_time_location
        neighbors = [(x + 1, y, time + 1), (x, y + 1, time + 1), (x - 1, y, time + 1), (x, y - 1, time + 1),
                     (x, y, time + 1)]
        neighbors = filter(self.is_in_bounds, neighbors)
        neighbors = filter(self.is_passable, neighbors)
        neighbors = filter(lambda next_location: self.is_collision_free(space_time_location, next_location, time),
                           neighbors)

        return list(neighbors)