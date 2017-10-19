"""This file contains a Trigram function that will create a Trigram on any given input"""
import io

trigrams = {}

def main(filepath = './sample.txt', words = 200):
    """Core function that calls the rest of the algorithms"""
    source_text = open_source(filepath)
    read_source(source_text)


def open_source(filepath):
    """Opens the source file"""
    source_text = ''
    with io.open(filepath, encoding = 'utf-8') as source_file:
        source_text = source_file.read()
    return source_text #return the text of the file


def read_source(text):
    """Reads the source file and builds trigrams"""
    source_text = text.split()
    print(source_text)
    text_length = len(source_text)
    for i in range(text_length - 2):
        key = source_text[i] + ' ' + source_text[i + 1]
        trigrams.setdefault(key, [])
        trigrams.get(key).append(source_text[i + 2])
    print(trigrams)

def generate_text(words):
    """Writes the text from given trigram"""


if __name__ == '__main__':
    """#todo FIll this in"""
    main()