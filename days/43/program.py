import argparse

# The add_argument() method is used to specify which command-line options the program is willing to accept.

# Positional Arguments (Required)
""" parser = argparse.ArgumentParser()
parser.add_argument(
    "square", help="display a squre of a given number", type=int)
args = parser.parse_args()
print(args.square**2) """

# Optional Arguments
# Adding action="store_true" turns --verbosity argument into more of a flag instead of something that requires a value.
""" parser = argparse.ArgumentParser()
parser.add_argument("-v",
                    "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on") """


# Combining Positional and Optional arguments
""" parser = argparse.ArgumentParser()

parser.add_argument(
    "square", type=int, help="display a squre of a given number")

parser.add_argument("-v",
                    "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("The square of {} equals {}".format(args.square, answer))
else:
    print(answer) """


# Added the 'count' action, which counts the number of times the argument is used. for example -vv equals 2 times.
# Added a default value for verbosity. Remember that by default, if an optional argument isn’t specified, it gets the None value, and that cannot be compared to an int value (hence the TypeError exception).

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2

if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
