from day import Day
from utilities.parse import Parse
class Day_2(Day):
    def __init__(self):
        self.input = self.puzzle_input()

    def parse_input(self):
        return [list(map(int, report.split())) for report in self.input.splitlines()]

    def part1(self):
        """Solve part 1."""
        reports = self.parse_input()
        safe_reports = 0

        for report in reports:
            increasing_or_decreasing = (report == sorted(report) or report == sorted(report, reverse=True))
            is_within_range = True
            for i in range(len(report)-1):
                level_diff = abs(report[i] - report[i+1])
                if not 1 <= level_diff <= 3:
                    is_within_range = False
            if increasing_or_decreasing and is_within_range:
                safe_reports += 1

        return safe_reports

    def part2(self):
        """Solve part 2."""
        return 0
