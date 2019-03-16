import functions
import argsparse

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

    # Extract text from file/string and assing it to new [list] variable
    original_text = functions.opener(text)  # list
    formatted_text = original_text[:]  # list

    # Execute function [spaces] if its flag is True
    if spaces:
        formatted_text = functions.spaces(formatted_text)

    # Execute function [capitals] if its flag is True
    if capitals:
        formatted_text = functions.capitals(formatted_text)

    # Execute function [statistics] if its flag is True, else assing None to variable
    statistic = functions.statisctics(formatted_text) if statistics else None

    #! Assemble text back to string before return/writing to file
    formatted_text = functions.assembler(formatted_text)

    # Execute function [mistakes] if its flag is True, else assing None to variable
    mistake = functions.mistakes(formatted_text) if mistakes else None

    # Writing to file if filepath in [out] is specified
    if out is not None:
        return statistic, mistake, functions.output(out, formatted_text)

    # Return text to console/terminal otherwise
    terminal_out = f"\n{30*'='}Output{30*'='}\n" + \
        formatted_text + f"\n{66*'='}\n"
    return terminal_out, statistic, mistake


# Unpacking tuple in [print]
print(*stedtxt(*args))
