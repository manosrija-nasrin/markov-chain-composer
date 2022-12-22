import os
import re
import string
import random

from graph import Graph, Vertex


def get_words_from_text(text_path):
    with open(text_path, 'rb') as f:
        text = f.read().decode("utf-8")  # text is a string

        # remove [text in here]
        # . any character
        # + one or more characters
        text = re.sub(r'\[(.+)\]', ' ', text)   # regex

        # replace multiple spaces and newlines with a single space
        text = ' '.join(text.split())
        text = text.lower()  # make everything lowercase to compare words easily

        # remove all punctuation [hello! it's me! --> hello its me]
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()  # split on spaces
    return words


def make_graph(words):
    g = Graph()

    previous_word = None

    # for each word
    for word in words:
        # check if that word is in the graph. if not, then add it.
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if it doesn't already exist
        # in the graph, otherwise increment weight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set our word to the previous word to iterate
        previous_word = word_vertex

    # generate the probability mapping before composing the graph
    g.generate_probability_mappings()

    return g


def compose(g: Graph, words: list, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))

    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):
    # step 1: get words from text
    # for text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    # words = words[:5000]

    words = []
    # for song lyrics
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)

    # step 2: make a graph using those words
    g = make_graph(words)

    # step 3: get the next word for x number of words (defined by user)
    composition = compose(g, words, 100)

    # step 4: show the user!
    return ' '.join(composition)  # return all words separated by a space


if __name__ == '__main__':
    print(main('queen'))
