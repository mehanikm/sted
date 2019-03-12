def opener(text_path: str):
    """Opens text_path file and return its text if exists, otherwise returns text_path"""
    try:
        with open(text_path, "rt") as file:
            text = file.read()
    except FileNotFoundError:
        print(
            f"File \"{text_path}\" was not found, processing \"{text_path}\" as text.")
        text = text_path
    return text


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
