def opener(text_path: str) -> list:
    """Opens text_path file and return its text as a list if exists, otherwise returns text_path as a list"""
    try:
        with open(text_path, "rt") as file:
            text = file.read()
    except FileNotFoundError:
        print(
            f"File \"{text_path}\" was not found, processing \"{text_path}\" as text.")
        text = text_path
    return list(text)


def assembler(text: list) -> str:
    """Assembles list elements to string"""
    new_text = ""
    for ch in text:
        new_text += ch
    return new_text


def spaces(text: list) -> list:
    """Removes excessive spaces in text"""
    c = 0
    separators = "\"\\!?.,;:'\n) "  # last space in this string is essential!
    # Correcting spaces inside text
    for i in range(len(text)):
        while text[i-c] == " " and (text[i + 1-c] in separators or text[i-1-c] in " (\n"):
            text.pop(i-c)
            c += 1
    # Stripping excessive whitespaces on ends of text
    while not text[0].isalpha():
        text.pop(0)
    while not text[-1].isalpha() and text[-1] not in "\"!?.;'":
        text.pop()
    return text


def capitals(text: list) -> list:
    """Converts first letter after [.] to uppercase unless it's placed after one of [abbreviations]"""
    abbreviations = ['al.', 'cd.', 'cdn.', 'col.', 'cykl.', 'cyt.',
                     'cz.', 'dosł.', 'godz.', 'iron.', 'itd.', 'itp.',
                     'jw.', 'jęz.', 'lic.', 'm.in.', 'mies.', 'mkw.',
                     'muz.', 'n.e.', 'n.p.m.', 'nast.', 'np.', 'nw.',
                     'o.o.', 'p.n.e.', 'p.o.', 'pl.', 'pn.', 'pt.', 'płd.',
                     'płn.', 'rys.', 'str.', 'tab.', 'tj.', 'tzn.',
                     'tzw.', 'wsch.', 'zach.', 'zob.', 'źr.', 'żeń.']
    # Converting to list of words instead of list of chars
    text_copy = assembler(text[:]).replace("\n", "\n ").split(" ")
    text = []
    # Converting to uppercase
    for i in range(len(text_copy)):
        if text_copy[i-1].endswith((".", ".\n")) and text_copy[i-1] not in abbreviations:
            text_copy[i] = text_copy[i].capitalize()

    # Creating list of chars
    for el in text_copy:
        if el.endswith("\n"):
            for l in el[:-1]:
                text.append(l)
            text.append("\n")
        else:
            for l in el:
                text.append(l)
            text.append(" ")
    # Return one-char list without last whitespace char
    return text[:-1]


def statisctics(text: list) -> str:
    """Returns string with further info:
        line count
        word count
        symbols count
        whitespaces count
    """
    lines = 1 + text.count("\n")

    whitespaces = 0
    for ws in ["\n", "\f", "\t", "\r", "\v", " "]:
        whitespaces += text.count(ws)

    symbs = len(text) - whitespaces
    words = len(assembler(text[:]).replace("\n", " ").strip().split(" "))
    return f"\n{20*'–'}\n{lines} lines\n{whitespaces} whitespaces\n{words} words\n{symbs} symbols\n{20*'–'}"


def output(path: str, text: str) -> None:
    """Writing output text to file"""
    try:
        # Text can be written only to following file extensions,
        # albeit program creates file with any extension
        if path.endswith((".txt", ".rtf", ".pdf", ".doc")):
            with open(path, "wt") as file:
                file.write(text)
            return f"\n-> Successfully written text to \"{path}\"!"
        else:
            raise EnvironmentError(
                0, "File extension must be either \".txt/.rtf/.pdf/.doc\"")
    # Handling raised in [try] block exeption
    except EnvironmentError as e:
        return f"\n-> Can't write to \"{path}\" file!\n{e}"
    return None
