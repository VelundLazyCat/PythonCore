import sys


def parse_args():
    result = ""

    result = " ".join(sys.argv[1:len(sys.argv)+1])

    return result
