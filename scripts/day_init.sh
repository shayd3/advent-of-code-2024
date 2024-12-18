#!/bin/sh
if [ -z "$1" ]
then
  echo "Please provide a day number"
  exit 1
fi

if ! command -v aoc &> /dev/null
then
    echo "aoc could not be found"
    echo "Please install aoc by running 'brew install scarvalhojr/tap/aoc-cli'. See https://github.com/scarvalhojr/aoc-cli for more information"
    exit 1
fi

day_number=$1

mkdir -p day_$day_number
touch day_$day_number/day_$day_number.py
cat <<EOF > day_$day_number/day_$day_number.py
# Day $day_number
from day import Day
from utilities.parse import Parse

class Day_$day_number(Day):
    def __init__(self):
        self.input = self.puzzle_input(is_example_input=True)

    def part_1(self):
        return

    def part_2(self):
        return

EOF

aoc download --input-file day_$day_number/input.txt --puzzle-file day_$day_number/puzzle.md --day $day_number

