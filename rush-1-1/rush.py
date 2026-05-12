import sys


def rush(x, y):
    """
    Display a square pattern based on x (width) and y (height)

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    try:
        if not isinstance(x, int) or not isinstance(y, int) or isinstance(x, bool) or isinstance(y, bool) or x <= 0 or y <= 0:
            print("Invalid size", file=sys.stderr)
            return

        for row in range(y):
            line = ""
            for col in range(x):
                is_top = row == 0
                is_bot = row == y - 1
                is_left = col == 0
                is_right = col == x - 1

                if (is_top or is_bot) and (is_left or is_right):
                    line += "o"
                elif is_top or is_bot:
                    line += "-"
                elif is_left or is_right:
                    line += "|"
                else:
                    line += " "
            print(line)
    except Exception:
        print("Invalid size", file=sys.stderr)
