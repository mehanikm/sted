import functions


def stedtxt(text: str, spaces=True, capitals=True, mistakes=True, statistics=False, out=None):
    """Main sted function

    Args:
        text(str): either path to text file or actual text
        spaces(bool): removes excessive spaces if True
        capitals(bool): replaces lowercase letter to uppercase where needed
        mistakes(bool): checks for mistakes in text
        statistics(bool): gives statistics of formatted text
        out(str OR None): path to output file, otherwise return formatted text as string
    Returns:
        None: if [out] arg is not None
        formatted_text(str): if [out] arg is None 
    """

    # Extract text from file/string and assing it to new [list] variable
    original_text = functions.opener(text)  # list
    formatted_text = original_text  # list

    # Execute function [spaces] if its flag is True
    if spaces:
        formatted_text = functions.spaces(formatted_text)

    # Execute function [capitals] if its flag is True
    if capitals:
        formatted_text = functions.capitals(formatted_text)

    # Execute function [statistics] if its flag is True, else assing None to variable
    statistic = functions.statisctics(formatted_text) if statistics else None

    # Assemble text back to string and return it
    formatted_text = functions.assembler(formatted_text)
    return formatted_text, statistic


print(*stedtxt("text.txt", statistics=True))
