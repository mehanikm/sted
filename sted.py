from functions import *


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

    if spaces:
        spaces(text)

    return None
