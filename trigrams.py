"""This file contains a Trigram function that will create a Trigram on any given input"""
import io

trigrams = {}

def main(filepath = './sample.txt', words = 200):
    """Core function that calls the rest of the algorithms"""
    source_text = open_source(filepath)
    print(source_text)
    read_source(source_text)

def open_source(filepath):
    """Opens the source file"""
    source_text = ''
    with io.open(filepath, encoding = 'utf-8') as source_file:
        source_text = source_file.read()

    return source_text
    #return the text of the file

def read_source(text):
    """Reads the source file and builds trigrams"""


def generate_text(words):
    """Writes the text from given trigram"""


if __name__ == '__main__':
#todo FIll this in
    main()