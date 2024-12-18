from day import Day
from utilities.parse import Parse
from collections import defaultdict

class Day_5(Day):
    def __init__(self):
        self.input = self.puzzle_input(is_example_input=False)

    def parse_input(self):
        page_rules, page_nums = self.input.split('\n\n')
        page_rules_dict = defaultdict(list)
        for rule in page_rules.split('\n'):
            key, value = map(int, rule.split('|'))
            page_rules_dict[key].append(value)
        page_nums = [list(map(int,nums.split(","))) for nums in page_nums.split('\n')]
        return page_rules_dict, page_nums

    def is_ordered(self, page_nums, page_rules):
        for i in range(1, len(page_nums)):
            if page_nums[i] not in page_rules[page_nums[i-1]]:
                return False
        return True

    def part1(self):
        page_rules, page_nums_list = self.parse_input()
        valid_page_num_lists = []

        for page_nums in page_nums_list:
            if self.is_ordered(page_nums, page_rules):
                valid_page_num_lists.append(page_nums)

        count = 0
        for valid_page_num_list in valid_page_num_lists:
            count += valid_page_num_list[len(valid_page_num_list)//2]

        return count

    def part2(self):
        page_rules, page_nums_list = self.parse_input()
        invalid_page_num_lists = []
        count = 0
        # find invalid_page_num_lists
        for page_nums in page_nums_list:
            if not self.is_ordered(page_nums, page_rules):
                invalid_page_num_lists.append(page_nums)

        # Fix the invalid_page_num_lists
        for invalid_page_num_list in invalid_page_num_lists:
            while not self.is_ordered(invalid_page_num_list, page_rules):
                for i in range(1, len(invalid_page_num_list)):
                    if invalid_page_num_list[i] not in page_rules[invalid_page_num_list[i-1]]:
                        invalid_page_num_list[i], invalid_page_num_list[i-1] = invalid_page_num_list[i-1], invalid_page_num_list[i]
                        break
            count += invalid_page_num_list[len(invalid_page_num_list)//2]
        return count
