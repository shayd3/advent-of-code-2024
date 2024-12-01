import sys
import importlib

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid input. Usage: solve.py <day>")
        sys.exit(1)

    day_number = sys.argv[1]
    module_name = f"day_{day_number}.day_{day_number}"

    try:
        day_module = importlib.import_module(module_name)
        day_class = getattr(day_module, f"Day_{day_number}")
        day = day_class()

        solution1 = day.part1()
        solution2 = day.part2()

        print("Part 1:", solution1)
        print("Part 2:", solution2)
    except ModuleNotFoundError:
        print(f"Day {day_number} not found.")
        sys.exit(1)
    except AttributeError:
        print(f"Day {day_number} does not have the required methods or class for day {day_number} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
