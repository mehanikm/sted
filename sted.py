import functions
import argsparse

import time

args = argsparse.args()


def stedtxt(text: str, spaces=False, capitals=False, mistakes=False, statistics=False, out=None) -> str:
    """Main sted function

    Args:
        text(str): either path to text file or actual text
        spaces(bool): removes excessive spaces
        capitals(bool): replaces lowercase letter to uppercase where needed
        mistakes(bool): checks for mistakes in text
        statistics(bool): gives statistics of formatted text
        out(str OR None): path to output file
    Returns:
        formatted_text(str), statistic(str): if [out] is None, print formatted text to
            console/terminal, statistic is optional, either a string or None
        statistic(str), output(str): if [out] is not None, returns the result of writing text to file
            attempt, statistic is optional, either a string or None
    """

    global total_time, spaces_t, capitals_t, stats_t, assembl_t, mistake_t  # ?Time

    # Extract text from file/string and assing it to new [list] variable
    opening_t = time.time()  # ?Time
    original_text = functions.opener(text)  # list
    formatted_text = original_text[:]  # list
    opening_t -= time.time()  # ?Time

    # Execute function [spaces] if its flag is True
    spaces_t = time.time()  # ?Time
    if spaces:
        formatted_text = functions.spaces(formatted_text)
    spaces_t -= time.time()  # ?Time

    # Execute function [capitals] if its flag is True
    capitals_t = time.time()  # ?Time
    if capitals:
        formatted_text = functions.capitals(formatted_text)
    capitals_t -= time.time()  # ?Time

    # Execute function [statistics] if its flag is True, else assing None to variable
    stats_t = time.time()  # ?Time
    statistic = functions.statisctics(formatted_text) if statistics else None
    stats_t -= time.time()  # ?Time

    #! Assemble text back to string before return/writing to file
    assembl_t = time.time()  # ?Time
    formatted_text = functions.assembler(formatted_text)
    assembl_t -= time.time()  # ?Time

    # Execute function [mistakes] if its flag is True, else assing None to variable
    mistake_t = time.time()  # ?Time
    mistake = functions.mistakes(formatted_text) if mistakes else None
    mistake_t -= time.time()  # ?Time

    # Writing to file if filepath in [out] is specified
    if out is not None:
        return statistic, mistake, functions.output(out, formatted_text)

    # Return text to console/terminal otherwise
    terminal_out = f"\n{30*'='}Output{30*'='}\n" + \
        formatted_text + f"\n{66*'='}\n"
    return terminal_out, statistic, mistake


# Unpacking tuple in [print]
print(*stedtxt(*args))
total_time = -spaces_t - capitals_t - stats_t - assembl_t - mistake_t
print("Time consumed:", total_time)
print("Spaces:", -spaces_t)
print("Capitals:", -capitals_t)
print("Stats:", -stats_t)
print("Mistakes:", -mistake_t)
print("Assemble:", -assembl_t)
