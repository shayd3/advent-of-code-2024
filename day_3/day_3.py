from day import Day
import re
class Day_3(Day):
    def __init__(self, is_example_input=False):
        self.input = self.puzzle_input(is_example_input)

    def find_mul(self, string):
        pattern = r"mul\(\d+,\d+\)"
        return re.findall(pattern, string)

    def find_mul_with_toggle(self, string):
        pattern = r"mul\(\d+,\d+\)|do(?:n't)?\(\)"
        return re.findall(pattern, string)

    def part1(self):
        result = 0
        found = self.find_mul(self.input)
        for f in found:
            nums = re.findall("\d+",f)
            result += int(nums[0]) * int(nums[1])
        return result

    def part2(self):
        result = 0
        found = self.find_mul_with_toggle(self.input)
        mul_enabled = True
        for f in found:
            if "mul" in f:
                if mul_enabled:
                    nums = re.findall("\d+",f)
                    result += int(nums[0]) * int(nums[1])
            elif "don't" in f:
                mul_enabled = False
            elif "do" in f:
                mul_enabled = True
        return result
