import fileinput
from panflute import *
from sys import stderr

ListOfHeaders = []

def Bold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))

def header_repeat(el, doc):
    if isinstance(el, Header):
        text = stringify (el)
        if text in ListOfHeaders:
            print ("Есть одинаковые заголовки: " + text, file = stderr)
        else:
            ListOfHeaders.append(text)

def header_level_pos(el, doc):
    if isinstance(el, Header) and el.level > 2:
        return Header(Str(stringify(el).upper()), level = el.level)


if __name__ == "__main__":
    run_filters ([header_repeat, header_level_pos], prepare = Bold)