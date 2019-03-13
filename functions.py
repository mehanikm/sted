def opener(text_path: str) -> list:
    """Opens text_path file and return its text as a list if exists, otherwise returns text_path as a list"""
    try:
        with open(text_path, "rt") as file:
            text = file.read()  # .replace("\n", " ")
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
    separators = "\"\\!?.,;:'\n) "
    for i in range(len(text)):
        while text[i-c] == " " and (text[i + 1-c] in separators or text[i-1-c] in " (\n"):
            text.pop(i-c)
            c += 1
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
    text_copy = assembler(text[:]).replace("\n", "\n ").split(" ")
    text = []
    # Converting to uppercase
    for i in range(len(text_copy)):
        if text_copy[i-1].endswith((".", ".\n")) and text_copy[i-1] not in abbreviations:
            text_copy[i] = text_copy[i].capitalize()

    # Creating list of single char elements
    for el in text_copy:
        if el.endswith("\n"):
            for l in el[:-1]:
                text.append(l)
            text.append("\n")
        else:
            for l in el:
                text.append(l)
            text.append(" ")
    return text[:-1]
