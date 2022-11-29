# Markov Chain Composer

Using Markov Chain to represent relationships between words in song lyrics and then generating new text from the graph. Implemented in Python.

### Status

Finished.

### Usage

In order to download this code, either click the green button at the top right and download as ZIP, or clone the repository. To run: `python3 compose.py` You'll have to slightly change some of the code in order to adjust length of composition/which file is the vocabulary for the composition.

In this folder, you will find the files:

- compose.py: reads text/song lyrics and generates new text of user-defined length
- graph.py - contains `Graph` class that implements the Markov chain

### Notes

The generated text is gibberish. A more intelligent implementation can be made by analysing the previous 3 words instead of just the previous word. Developments (if made) will be in a separate project.

### Credits

- [12 Beginner Python Projects - Coding Course](https://youtu.be/8ext9G7xspg?t=7534) by freeCodeCamp ([Kylie Ying](https://www.youtube.com/ycubed))
- [Kylie Ying's repository that contains templates for `graph.py` and `compose.py`](https://github.com/kying18/graph-composer/)
