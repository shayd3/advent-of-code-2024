from day import Day
from utilities.parse import Parse
class Day_2(Day):
    def __init__(self):
        self.input = self.puzzle_input(is_example_input=False)

    def parse_input(self):
        return [list(map(int, report.split())) for report in self.input.splitlines()]

    def is_good_report(self, report: list) -> bool:
        increasing_or_decreasing = (report == sorted(report) or report == sorted(report, reverse=True))
        is_within_range = True
        for i in range(len(report)-1):
            level_diff = abs(report[i] - report[i+1])
            if not 1 <= level_diff <= 3:
                is_within_range = False
        return increasing_or_decreasing and is_within_range

    def part1(self):
        """Solve part 1."""
        reports = self.parse_input()
        safe_reports = 0

        for report in reports:
            if self.is_good_report(report):
                safe_reports += 1
        return safe_reports

    def part2(self):
        """Solve part 2."""
        reports = self.parse_input()
        safe_reports = 0

        for report in reports:
            is_good = False
            for j in range(len(report)):
                # new list => (all elements excluding j) + all elements from j + 1 to end of list
                # Essentially going through all possibilities of each element being removed
                report_one_removed = report[:j] + report[j+1:]
                if self.is_good_report(report_one_removed):
                    # at least one removed in the list made the report good
                    is_good = True
            if is_good:
                safe_reports += 1
        return safe_reports
