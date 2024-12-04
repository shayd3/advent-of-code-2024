from abc import ABC, abstractmethod
from pathlib import Path

class Day(ABC):
    def puzzle_input(self, is_example_input = False):
        """Grabs the input file for the day which is at the root of the folder"""
        # Get the directory of the current module
        module_dir = Path(self.__class__.__module__.replace('.', '/')).parent
        # Construct the path to the input.txt file within the same directory
        input_file = module_dir / "example.txt" if (is_example_input) else module_dir / "input.txt"
        return input_file.read_text().strip()

    @abstractmethod
    def part1(self, data: any):
        """Solve part 1."""
        pass

    @abstractmethod
    def part2(self, data: any):
        """Solve part 2."""
        pass
