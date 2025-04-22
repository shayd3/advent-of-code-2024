# Day 6
from day import Day
from utilities.parse import Parse

class Day_6(Day):
    def __init__(self, is_example_input=False):
        self.input = self.puzzle_input(is_example_input)

    def parse_input(self):
        guard_position = (0, 0)
        lab_map = []

        lines = self.input.split('\n')
        for i, line in enumerate(lines):
            lab_map.append([])
            for j, char in enumerate(line):
                lab_map[i].append(LabMapPosition(is_obstacle = char == "#", is_visited = False))
                if char == "^":
                    guard_position = (i, j)
                    lab_map[i][j].is_visited = True
        return lab_map, guard_position

    def is_not_edge(self, position, lab_map):
        top_edge = position[0] > 0
        bottom_edge = position[0] < len(lab_map) - 1
        left_edge = position[1] > 0
        right_edge = position[1] < len(lab_map[0]) - 1
        return top_edge and bottom_edge and left_edge and right_edge

    def need_to_turn_right(self, gp, direction, lab_map):
        if direction == 0:
            return lab_map[gp[0] - 1][gp[1]].is_obstacle
        elif direction == 1:
            return lab_map[gp[0]][gp[1] + 1].is_obstacle
        elif direction == 2:
            return lab_map[gp[0] + 1][gp[1]].is_obstacle
        elif direction == 3:
            return lab_map[gp[0]][gp[1] - 1].is_obstacle

    def move_guard(self, gp, direction):
        if direction == 0:
            return (gp[0] - 1, gp[1])
        elif direction == 1:
            return (gp[0], gp[1] + 1)
        elif direction == 2:
            return (gp[0] + 1, gp[1])
        elif direction == 3:
            return (gp[0], gp[1] - 1)

    def turn_right(self, direction):
        # 0 = up, 1 = right, 2 = down, 3 = left
        return (direction + 1) % 4

    def part1(self):
        lab_map, gp = self.parse_input()
        unique_positions_visted = 1 # start at one since the guard is already at the first position
        print(gp)
        direction = 0

        while(self.is_not_edge(gp, lab_map)):
            if gp == (7, 7):
                print("here")
            # look foward in the direction guard is facing to see if we need to turn right before moving
            if self.need_to_turn_right(gp, direction, lab_map):
                direction = self.turn_right(direction)
            gp = self.move_guard(gp, direction)

            if not lab_map[gp[0]][gp[1]].is_visited:
                unique_positions_visted += 1
                lab_map[gp[0]][gp[1]].is_visited = True
        return unique_positions_visted

    def part2(self):
        return

class LabMapPosition():
    def __init__(self, is_obstacle, is_visited):
        self.is_obstacle = is_obstacle
        self.is_visited = is_visited
