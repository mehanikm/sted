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
