from day import Day
import re
class Day_3(Day):
    def __init__(self):
        self.input = self.puzzle_input(is_example_input=False)

    def part1(self):
        result = 0
        found = re.findall("mul\(\d+,\d+\)",self.input)
        for f in found:
            nums = re.findall("\d+",f)
            result += int(nums[0]) * int(nums[1])
        return result

    def part2(self):
        return 0
