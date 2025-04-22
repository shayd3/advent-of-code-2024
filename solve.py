import sys
import importlib

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Invalid input. Usage: solve.py <day> <is_example (True/False)>")
        sys.exit(1)

    day_number = sys.argv[1]
    is_example = sys.argv[2] if len(sys.argv) > 2 else False
    module_name = f"day_{day_number}.day_{day_number}"

    try:
        day_module = importlib.import_module(module_name)
        day_class = getattr(day_module, f"Day_{day_number}")
        day = day_class(is_example_input=is_example.lower() == 'true')

        solution1 = day.part1()
        solution2 = day.part2()

        print("Part 1:", solution1)
        print("Part 2:", solution2)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
