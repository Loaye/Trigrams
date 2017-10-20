"""This file contains a Trigram function that will create a Trigram on any given input"""
import io 
import random
import sys


def main(filepath = './sample.txt', words = 200):
    """Core function that calls the rest of the algorithms"""
    source_text = open_source(filepath)
    trigrams = make_trigrams(source_text)
    generate_text(trigrams, words)


def open_source(filepath):
    """Opens the source file"""
    source_text = ''
    with io.open(filepath, encoding = 'utf-8') as source_file:
        source_text = source_file.read()
    return source_text #return the text of the file


def make_trigrams(text):
    """Reads the source file and builds trigrams"""
    trigrams = {}
    source_text = text.split()

    text_length = len(source_text)
    for i in range(text_length - 2):
        key = source_text[i] + ' ' + source_text[i + 1]
        trigrams.setdefault(key, [])
        trigrams.get(key).append(source_text[i + 2])
        
    return trigrams
    

def generate_text(trigrams, words):
    """Writes the text from given trigram"""
    wordlist = []
    keylist = list(trigrams.keys())
    start_words = random.choice(keylist).split(" ")
    wordlist.append(start_words[0])
    wordlist.append(start_words[1])

    while(len(wordlist) < words):
        search_key = wordlist[-2] + " " + wordlist[-1]
        v_possibilities = trigrams.get(search_key)
        if v_possibilities == None:
            break

        wordlist.append(random.choice(v_possibilities))

    output_text = " ".join(wordlist)

    print(output_text)
    return output_text


if __name__ == '__main__':
    """Main entry point"""
    main(sys.argv[1], int(sys.argv[2]))