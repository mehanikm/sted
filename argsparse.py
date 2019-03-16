import argparse
import sys


def args():
    parser = argparse.ArgumentParser(
        description="Stream text editor. Edits input \
        text(text file) on the fly and outputs either to terminal or to file. ",
        usage=f"python3 {sys.argv[0]} path/text [-h] [-s] [-c] [-m] [-t] [-o path]"
    )
    # Adding arguments
    # Setting all optional args to False with "default", and True if called with "const"
    # Input file
    parser.add_argument("input", metavar="path/text", nargs=1,
                        help="Path to source file/Text itself")
    # Spaces func
    parser.add_argument("-s", "--spaces", required=False, action="store_const", const=True,
                        default=False, help="Removes excessive spaces in text")
    # Capitals func
    parser.add_argument("-c", "--capitals", required=False, default=False, action="store_const",
                        const=True, help="Converts first letter after '.' to uppercase")
    # Mistakes func
    parser.add_argument("-m", "--mistakes", required=False, default=False,
                        action="store_const", const=True, help="Returns mistakes and its number")
    # Statistics
    parser.add_argument("-t", "--stats", required=False, default=False, action="store_const",
                        const=True, help="Returns number of lines, words, symbols and whitespaces")
    # Output file
    parser.add_argument("-o", "--output", required=False, metavar="path",
                        default=None, help="Path to output file('.txt', '.rtf', '.pdf' or '.doc')")

    # parse args to variables
    args = parser.parse_args()
    inp = args.input[0]
    space = args.spaces
    capital = args.capitals
    mistake = args.mistakes
    stats = args.stats
    outp = args.output
    return inp, space, capital, mistake, stats, outp
