# sted
Stream text editor.

Can edit input files or input strings.

Options:
  <path/text>: essential positional option, path to source file or text itself.
  -s, --spaces: Removes excessive spaces in text before/after separators, multiple spaces etc.
  -c, --capitals: Replaces lowercase letters with uppercase where they must be.
  -m, --mistakes: Looks for every word in dict and returns it and its index to terminal if not found.
  -t, --stats: Returns # of lines, words, spaces and symbols to terminal.
  
  -o, output <path>: Writes result to path file(only text).
  
  Examples:
    python3 sted.py book.txt -sctm -o book_new.txt
    python3 sted.py text.txt -sco newtext.txt
    python3 sted.py to_console.txt -sctm 
