#!/usr/bin/python3
import sys, ast, os

file_stack = []
file_set = set()
if (len(sys.argv) != 2):
    sys.exit("Usage: flattener.py FILENAME")
file_param = os.path.realpath(sys.argv[1])
filename = os.path.basename(file_param)
# Get into the contract's directory
os.chdir(os.path.dirname(file_param))
file_stack.append(open(filename, "r"))
file_set.add(filename)

while file_stack:
    # Files are iterators themselves
    for line in file_stack[-1]:
        if (line.startswith("import ")):
            include = line.strip().split()[-1].rstrip(';')
            contract = ast.literal_eval(include)
            if contract.startswith("."):
                contract = os.path.join(os.path.dirname(file_stack[-1].name), contract)
            if (not any(os.path.samefile(contract, p) for p in file_set)):
                file_set.add(contract)
                file_stack.append(open(contract, "r"))
                break
        else:
            print(line, end='')
    else:
        print()
        file_stack.pop()
