import sys


def help_print(prog_name):
    print("{0} [ARG0] [ARG1] [ARG2] ...".format(prog_name))
    print("- Need arguments...")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        help_print(sys.argv[0])
        sys.exit()

    # sys.argv[0], ...
    print('sys.argv is list data structure.')
    print(sys.argv)
