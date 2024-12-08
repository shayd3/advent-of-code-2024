from day import Day
from utilities.parse import Parse
from collections import defaultdict

class Day_4(Day):
    def __init__(self):
        self.input = self.puzzle_input(is_example_input=False)

    def parse_input(self):
        return Parse.to_2d_list(self.input)

    def part1(self):
        wordsearch = self.parse_input()
        occurances = 0
        word_dict = defaultdict(str)

        for row_index, row in enumerate(wordsearch):
            for col_index, letter in enumerate(row):
                word_dict[row_index, col_index] = letter

        coords = list(word_dict.keys())
        coord_offsets = -1,0,1

        for i,j in coords:
            for x_offset in coord_offsets:
                for y_offset in coord_offsets:
                    word = ""
                    for n in range(4):
                        word += word_dict[i+x_offset*n, j+y_offset*n]
                    if word == "XMAS":
                        occurances += 1

        return occurances

    def part2(self):
        return 0
