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

    def part1(self):
        page_rules, page_nums_list = self.parse_input()
        valid_page_num_lists = []

        for page_nums in page_nums_list:
            valid = True
            for i in range(1, len(page_nums)):
                if page_nums[i] not in page_rules[page_nums[i-1]]:
                    valid = False
                    break
            if valid:
                valid_page_num_lists.append(page_nums)

        middle_page_count = 0
        # get middle page number and add to middle_page_count
        for valid_page_num_list in valid_page_num_lists:
            middle_page_count += valid_page_num_list[len(valid_page_num_list)//2]

        return middle_page_count

    def part2(self):
        return 0
