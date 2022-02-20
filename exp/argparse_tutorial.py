import argparse
parser = argparse.ArgumentParser()
parser.add_argument('bar', nargs='+', help='bar help')
args = parser.parse_args()

# Check commands
if args.bar[0] == "commit":
    print(args.bar[0])