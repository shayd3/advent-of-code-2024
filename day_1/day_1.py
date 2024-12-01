from day import Day
from utilities.parse import Parse
from collections import Counter
from typing import List

class Day_1(Day):
    def __init__(self):
        self.input = self.puzzle_input()

    def parse_input(self) -> List[int]:
        left_list, right_list = [], []
        for pair in Parse.str_to_list(self.input):
            left, right = pair.split("   ")
            left_list.append(int(left))
            right_list.append(int(right))
        return left_list, right_list

    def part1(self):
        """Solve part 1."""
        distance_total = 0
        left_list, right_list = self.parse_input()

        for left, right in zip(sorted(left_list), sorted(right_list)):
            distance_total += abs(left - right)

        return distance_total

    def part2(self):
        """Solve part 2."""
        similarity_score = 0
        left_list, right_list = self.parse_input()

        for left in left_list:
            similarity_score += left * Counter(right_list)[left]

        return similarity_score
